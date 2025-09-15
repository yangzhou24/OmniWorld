import numpy as np
from plyfile import PlyData, PlyElement
import imageio
from pathlib import Path
import json
from scipy.spatial.transform import Rotation as R

def project(intrinsics, extrinsics, depths):
    N, H, W = depths.shape
    pixels = get_pixel(H, W)[None].repeat(N, axis=0)            # shape: (N, 3, HW)

    local_points = np.einsum('nij, njk -> nki', np.linalg.inv(intrinsics), pixels) * depths.reshape(N, H*W, 1)      # shape: (N, HW, 3)
    local_points = np.concatenate([local_points, np.ones_like(local_points[..., 0:1])], axis=-1)
    global_points = np.einsum('nij, nkj -> nki', se3_inverse(extrinsics), local_points)[..., :3]

    return global_points.reshape(N, H, W, 3)

def se3_inverse(T):
    """
    Computes the inverse of a batch of SE(3) matrices.
    """
    R = T[..., :3, :3]
    t = T[..., :3, 3, np.newaxis]

    R_inv = np.swapaxes(R, -2, -1)
    t_inv = -R_inv @ t

    bottom_row = np.zeros((*T.shape[:-2], 1, 4), dtype=T.dtype)
    bottom_row[..., :, 3] = 1

    top_part = np.concatenate([R_inv, t_inv], axis=-1)
    T_inv = np.concatenate([top_part, bottom_row], axis=-2)

    return T_inv

def load_split_info(scene_dir: Path):
    """Return the split json dict."""
    with open(scene_dir / "split_info.json", "r", encoding="utf-8") as f:
        return json.load(f)

def load_camera_poses(scene_dir: Path, split_idx: int):
    """
    Returns
    -------
    intrinsics : (S, 3, 3) array, pixel-space K matrices
    extrinsics : (S, 4, 4) array, OpenCV camera-to-world matrices
    """
    # ----- read metadata -----------------------------------------------------
    split_info = load_split_info(scene_dir)
    idxs = split_info["split"][split_idx]
    frame_count = len(idxs)

    cam_file = scene_dir / "camera" / f"split_{split_idx}.json"
    with open(cam_file, "r", encoding="utf-8") as f:
        cam = json.load(f)

    # ----- intrinsics --------------------------------------------------------
    intrinsics = np.repeat(np.eye(3)[None, ...], frame_count, axis=0)
    intrinsics[:, 0, 0] = cam["focals"]          # fx
    intrinsics[:, 1, 1] = cam["focals"]          # fy
    intrinsics[:, 0, 2] = cam["cx"]              # cx
    intrinsics[:, 1, 2] = cam["cy"]              # cy

    # ----- extrinsics --------------------------------------------------------
    extrinsics = np.repeat(np.eye(4)[None, ...], frame_count, axis=0)

    # SciPy expects quaternions as (x, y, z, w) → convert
    quat_wxyz = np.array(cam["quats"])           # (S, 4)  (w,x,y,z)
    quat_xyzw = np.concatenate([quat_wxyz[:, 1:], quat_wxyz[:, :1]], axis=1)

    rotations = R.from_quat(quat_xyzw).as_matrix()      # (S, 3, 3)
    translations = np.array(cam["trans"])               # (S, 3)

    extrinsics[:, :3, :3] = rotations
    extrinsics[:, :3, 3] = translations

    return intrinsics.astype(np.float32), extrinsics.astype(np.float32), idxs


def load_depth(depthpath):
    """
    Returns
    -------
    depthmap : (H, W) float32
    valid   : (H, W) bool      True for reliable pixels
    """

    depthmap = imageio.v2.imread(depthpath).astype(np.float32) / 65535.0
    near_mask = depthmap < 0.0015   # 1. too close
    far_mask = depthmap > (65500.0 / 65535.0) # 2. filter sky
    # far_mask = depthmap > np.percentile(depthmap[~far_mask], 95) # 3. filter far area (optional)
    near, far = 1., 1000.
    depthmap = depthmap / (far - depthmap * (far - near)) / 0.004

    valid = ~(near_mask | far_mask)
    depthmap[~valid] = -1

    return depthmap, valid

def get_pixel(H, W):
    # get 2D pixels (u, v) for image_a in cam_a pixel space
    u_a, v_a = np.meshgrid(np.arange(W), np.arange(H))
    # u_a = np.flip(u_a, axis=1)
    # v_a = np.flip(v_a, axis=0)
    pixels_a = np.stack([
        u_a.flatten() + 0.5, 
        v_a.flatten() + 0.5, 
        np.ones_like(u_a.flatten())
    ], axis=0)
    
    return pixels_a

def rotate_target_dim_to_last_axis(x, target_dim=3):
    shape = x.shape
    axis_to_move = -1
    # Iterate backwards to find the first occurrence from the end 
    # (which corresponds to the last dimension of size 3 in the original order).
    for i in range(len(shape) - 1, -1, -1):
        if shape[i] == target_dim:
            axis_to_move = i
            break

    # 2. If the axis is found and it's not already in the last position, move it.
    if axis_to_move != -1 and axis_to_move != len(shape) - 1:
        # Create the new dimension order.
        dims_order = list(range(len(shape)))
        dims_order.pop(axis_to_move)
        dims_order.append(axis_to_move)
        
        # Use permute to reorder the dimensions.
        ret = x.transpose(*dims_order)
    else:
        ret = x

    return ret


def write_ply(
    xyz,
    rgb=None,
    path='output.ply',
) -> None:
    if rgb is not None and rgb.max() > 1:
        rgb = rgb / 255.

    xyz = rotate_target_dim_to_last_axis(xyz, 3)
    xyz = xyz.reshape(-1, 3)

    if rgb is not None:
        rgb = rotate_target_dim_to_last_axis(rgb, 3)
        rgb = rgb.reshape(-1, 3)
    
    if rgb is None:
        min_coord = np.min(xyz, axis=0)
        max_coord = np.max(xyz, axis=0)
        normalized_coord = (xyz - min_coord) / (max_coord - min_coord + 1e-8)
        
        hue = 0.7 * normalized_coord[:,0] + 0.2 * normalized_coord[:,1] + 0.1 * normalized_coord[:,2]
        hsv = np.stack([hue, 0.9*np.ones_like(hue), 0.8*np.ones_like(hue)], axis=1)

        c = hsv[:,2:] * hsv[:,1:2]
        x = c * (1 - np.abs( (hsv[:,0:1]*6) % 2 - 1 ))
        m = hsv[:,2:] - c
        
        rgb = np.zeros_like(hsv)
        cond = (0 <= hsv[:,0]*6%6) & (hsv[:,0]*6%6 < 1)
        rgb[cond] = np.hstack([c[cond], x[cond], np.zeros_like(x[cond])])
        cond = (1 <= hsv[:,0]*6%6) & (hsv[:,0]*6%6 < 2)
        rgb[cond] = np.hstack([x[cond], c[cond], np.zeros_like(x[cond])])
        cond = (2 <= hsv[:,0]*6%6) & (hsv[:,0]*6%6 < 3)
        rgb[cond] = np.hstack([np.zeros_like(x[cond]), c[cond], x[cond]])
        cond = (3 <= hsv[:,0]*6%6) & (hsv[:,0]*6%6 < 4)
        rgb[cond] = np.hstack([np.zeros_like(x[cond]), x[cond], c[cond]])
        cond = (4 <= hsv[:,0]*6%6) & (hsv[:,0]*6%6 < 5)
        rgb[cond] = np.hstack([x[cond], np.zeros_like(x[cond]), c[cond]])
        cond = (5 <= hsv[:,0]*6%6) & (hsv[:,0]*6%6 < 6)
        rgb[cond] = np.hstack([c[cond], np.zeros_like(x[cond]), x[cond]])
        rgb = (rgb + m)

    dtype = [
        ("x", "f4"),
        ("y", "f4"),
        ("z", "f4"),
        ("nx", "f4"),
        ("ny", "f4"),
        ("nz", "f4"),
        ("red", "u1"),
        ("green", "u1"),
        ("blue", "u1"),
    ]
    normals = np.zeros_like(xyz)
    elements = np.empty(xyz.shape[0], dtype=dtype)
    attributes = np.concatenate((xyz, normals, rgb * 255), axis=1)
    elements[:] = list(map(tuple, attributes))
    vertex_element = PlyElement.describe(elements, "vertex")
    ply_data = PlyData([vertex_element])
    ply_data.write(path)
from utils import *
import os
from tqdm import tqdm
import argparse

if __name__ == "__main__":
    # 1. Set up the argument parser
    parser = argparse.ArgumentParser(description="Load scene data and generate a point cloud.")
    parser.add_argument("scene_path", type=str, help="Path to the scene directory.")
    parser.add_argument("--split_idx", type=int, default=0, help="Split index to use for camera poses.")
    
    # 2. Parse the arguments from the command line
    args = parser.parse_args()

    # 3. Use the parsed path instead of a hardcoded one
    scene = Path(args.scene_path)
    if not scene.is_dir():
        print(f"Error: Path '{scene}' is not a valid directory.")
        exit()

    split_idx = args.split_idx

    K, w2c, idxs = load_camera_poses(scene, split_idx=split_idx)
    print(f"Loaded {len(idxs)} frames from scene: {scene.name}")

    depths = []
    rgbs = []
    masks = []
    for idx in tqdm(idxs, desc='Loading image and depth..'):
        depth, mask = load_depth(os.path.join(scene, 'depth', f'{idx:06d}.png'))
        rgb = imageio.v2.imread(os.path.join(scene, 'color', f'{idx:06d}.png'))

        rgbs.append(rgb)
        depths.append(depth)
        masks.append(mask)

    rgbs = np.stack(rgbs, axis=0)
    depths = np.stack(depths, axis=0)
    masks = np.stack(masks, axis=0)

    points = project(intrinsics=K, extrinsics=w2c, depths=depths)

    # Save the output file in the scene directory
    save_path = scene / f'split{split_idx}_points.ply'
    write_ply(points[masks].reshape(-1, 3)[::50], rgbs[masks].reshape(-1, 3)[::50], path=save_path)
    print(f'✅ Saved point cloud to {save_path}')
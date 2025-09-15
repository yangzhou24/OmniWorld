scene_id=1e527547f893
root=/path/to/DATA_PATH        # where you store OmniWorld

mkdir -p ${scene_id}

# --- RGB (may span several parts) ------------------------------------------
for rgb_tar in ${root}/videos/OmniWorld-Game/${scene_id}/${scene_id}_rgb_*.tar.gz
do
    echo "Extracting $(basename $rgb_tar)…"
    tar -xzf "$rgb_tar" -C ${scene_id}
done

# --- Depth -----------------------------------------------------------------
for d_tar in ${root}/annotations/OmniWorld-Game/${scene_id}/${scene_id}_depth_*.tar.gz
do
    echo "Extracting $(basename $d_tar)…"
    tar -xzf "$d_tar" -C ${scene_id}
done

# --- Flow ------------------------------------------------------------------
for f_tar in ${root}/annotations/OmniWorld-Game/${scene_id}/${scene_id}_flow_*.tar.gz
do
    echo "Extracting $(basename $f_tar)…"
    tar -xzf "$f_tar" -C ${scene_id}
done

# --- All other annotations --------------------------------------
tar -xzf ${root}/annotations/OmniWorld-Game/${scene_id}/${scene_id}_others.tar.gz -C ${scene_id}
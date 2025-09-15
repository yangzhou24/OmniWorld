<h1 align='center'>OmniWorld: A Multi-Domain and Multi-Modal Dataset for 4D World Modeling</h1>
<div align='center'>
    <a href='https://github.com/yangzhou24' target='_blank'>Yang Zhou</a><sup>1</sup> 
    <a href='https://github.com/yyfz' target='_blank'>Yifan Wang</a><sup>1</sup> 
    <a href='https://zhoutimemachine.github.io' target='_blank'>Jianjun Zhou</a><sup>1,2</sup> 
    <a href='hhttps://github.com/AmberHeart' target='_blank'>Wenzheng Chang</a><sup>1</sup> 
    <a href='https://github.com/ghy0324' target='_blank'>Haoyu Guo</a><sup>1</sup> 
    <a href='https://github.com/LiZizun' target='_blank'>Zizun Li</a><sup>1</sup> 
    <a href='https://kaijing.space/' target='_blank'>Kaijing Ma</a><sup>1</sup> 
    
</div>
<div align='center'>
<a target='_blank'>Xinyue Li</a><sup>1</sup> 
    <a href='https://scholar.google.com/citations?user=5SuBWh0AAAAJ&hl=en' target='_blank'>Yating Wang</a><sup>1</sup> 
    <a href='https://www.haoyizhu.site/' target='_blank'>Haoyi Zhu</a><sup>1</sup> 
    <a href='https://mingyulau.github.io/' target='_blank'>Mingyu Liu</a><sup>1,2</sup> 
    <a target='_blank'>Dingning Liu</a><sup>1</sup> 
    <a href='https://yangjiangeyjg.github.io/' target='_blank'>Jiange Yang</a><sup>1</sup> 
    <a href='https://sotamak1r.github.io/' target='_blank'>Junyi Chen</a><sup>1</sup> 
</div>
<div align='center'>
    <a href='https://github.com/Kr1sJFU' target='_blank'>Zhoujie Fu</a><sup>1</sup> 
    <a href='https://cshen.github.io' target='_blank'>Chunhua Shen</a><sup>1,2</sup> 
    <a href='https://oceanpang.github.io' target='_blank'>Jiangmiao Pang</a><sup>1</sup> 
    <a href='https://kpzhang93.github.io/' target='_blank'>Kaipeng Zhang</a><sup>1</sup>
    <a href='https://tonghe90.github.io/' target='_blank'>Tong He</a><sup>1†</sup>
</div>
<div align='center'>
    <sup>1</sup>Shanghai AI Lab  <sup>2</sup>ZJU 
</div>
<br>
<div align="center">
  <a href="https://yangzhou24.github.io/OmniWorld/"><img src="https://img.shields.io/badge/Project Page-F78100?style=plastic&logo=google-chrome&logoColor=white"></a>  
  <a href="https://arxiv.org/abs/xxx"><img src="https://img.shields.io/static/v1?label=Paper&message=Arxiv&color=red&logo=arxiv"></a>  
  <a href="https://github.com/yangzhou24/OmniWorld"><img src="https://img.shields.io/static/v1?label=Code&message=Github&color=blue&logo=github"></a>  
  <a href="https://huggingface.co/datasets/InternRobotics/OmniWorld"><img src="https://img.shields.io/static/v1?label=Dataset&message=HuggingFace&color=yellow&logo=huggingface"></a>  
</div>

<img src="assets/teaser.png" width="1000px">

## 🎉 NEWS
- [2025.9.16] 🔥 The first 1.2k splits release of OmniWorld-Game is now live on Hugging Face! More data is coming soon, stay tuned!

## ✨ Abstract
The field of 4D world modeling—aiming to jointly capture spatial geometry and temporal dynamics—has witnessed remarkable progress in recent years, driven by advances in large-scale generative models and multimodal learning.
However, the development of truly general 4D world models remains fundamentally constrained by the availability of high-quality data.
Existing datasets and benchmarks often lack the dynamic complexity, multi-domain diversity, and spatial–temporal annotations required to support key tasks such as 4D geometric reconstruction, future prediction, and camera-control video generation.
To address this gap, we introduce _OmniWorld_, a large-scale, multi-domain, multi-modal dataset specifically designed for 4D world modeling.
_OmniWorld_ consists of a newly collected _OmniWorld-Game_ dataset and several curated public datasets spanning diverse domains.
Compared with existing synthetic datasets, _OmniWorld-Game_ provides richer modality coverage, larger scale, and more realistic dynamic interactions.
Based on this dataset, we establish a challenging benchmark that exposes the limitations of current state-of-the-art (SOTA) approaches in modeling complex 4D environments.
Moreover, fine-tuning existing SOTA methods on _OmniWorld_ leads to significant performance gains across 4D reconstruction and video generation tasks, strongly validating _OmniWorld_ as a powerful resource for training and evaluation.
We envision _OmniWorld_ as a catalyst for accelerating the development of general-purpose 4D world models, ultimately advancing machines’ holistic understanding of the physical world.


## 💡 Dataset Download
You can download the entire OmniWorld dataset using the following command:
```bash
# 1. Install (if you haven't yet)
pip install --upgrade "huggingface_hub[cli]"

# 2. Full download
hf download InternRobotics/OmniWorld \
           --repo-type dataset \
           --local-dir /path/to/DATA_PATH
```
For downloading specific files (instead of the full dataset), please refer to the [`dowanload_specific.py`](scripts/dowanload_specific.py).



## 🚀 Visualize as Point Cloud

This script allows you to convert a scene from the dataset into a 3D point cloud for inspection.

### 1\. Prerequisites

Please follow the instructions in the "Dataset Download" section to acquire the dataset.

### 2\. Data Structure

Ensure your data is structured correctly. Each scene directory should contain the following subdirectories and files:

```
<your-data-path>/b04f88d1f85a/
├─ color/              # RGB frames (.png)
├─ depth/              # 16-bit depth maps
├─ flow/               # flow_u_16.png / flow_v_16.png / flow_vis.png
├─ camera/             # split_*.json (intrinsics + extrinsics)
├─ subject_masks/      # foreground masks (per split)
├─ gdino_mask/         # dynamic-object masks (per frame)
├─ text/               # structured captions (81-frame segments)
├─ droidclib/          # coarse camera poses (if you need them)
├─ fps.txt             # source video framerate
└─ split_info.json     # how frames are grouped into splits
```

### 3\. Usage

Run the `visualize_pcd.py` script, providing the path to the scene and the desired split index.

**Example:**

```bash
python scripts/visualize_pcd.py <your-data-path>/b04f88d1f85a --split_idx 0
```

The output point cloud will be saved to `<your-data-path>/b04f88d1f85a/split0_points.ply`. You can view this file using a 3D viewer like [MeshLab](https://www.meshlab.net/).

## 📄 License
The OmniWorld dataset is released under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)**. By accessing or using this dataset, you agree to be bound by the terms and conditions outlined in this license, as well as the specific provisions detailed below.

- **Special Note on Third-Party Content**:
A portion of this dataset is derived from third-party game content. All intellectual property rights pertaining to these original game assets (including, but not limited to, RGB and depth images) remain with their respective original game developers and publishers.

- **Permitted Uses**:
You are hereby granted permission, free of charge, to use, reproduce, and share the OmniWorld dataset and any adaptations thereof, solely for non-commercial research and educational purposes. This includes, but is not limited to: academic publications, algorithm benchmarking, reproduction of scientific results.

Under this license, you are expressly **forbidden** from:

- Using the dataset, in whole or in part, for any commercial purpose, including but not limited to its incorporation into commercial products, services, or monetized applications.

- Redistributing the original third-party game assets contained within the dataset outside the scope of legitimate research sharing.
Removing or altering any copyright, license, or attribution notices.

The authors of the OmniWorld dataset provide this dataset "as is" and make no representations or warranties regarding the legality of the underlying data for any specific purpose. Users are solely responsible for ensuring that their use of the dataset complies with all applicable laws and the terms of service or license agreements of the original game publishers (sources of third-party content).

For the full legal text of the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License, please visit: https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.

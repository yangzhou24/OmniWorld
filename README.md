<h1 align='center'>OmniWorld: A Multi-Domain and Multi-Modal Dataset for 4D World Modeling</h1>
<div align='center'>
    <a href='https://github.com/yangzhou24' target='_blank'>Yang Zhou</a><sup>1</sup> 
    <a href='https://github.com/yyfz' target='_blank'>Yifan Wang</a><sup>1</sup> 
    <a href='https://zhoutimemachine.github.io' target='_blank'>Jianjun Zhou</a><sup>1,2</sup> 
    <a href='https://github.com/AmberHeart' target='_blank'>Wenzheng Chang</a><sup>1</sup> 
    <a href='https://github.com/ghy0324' target='_blank'>Haoyu Guo</a><sup>1</sup> 
    <a href='https://github.com/LiZizun' target='_blank'>Zizun Li</a><sup>1</sup> 
    <a href='https://kaijing.space/' target='_blank'>Kaijing Ma</a><sup>1</sup> 
    
</div>
<div align='center'>
<a href='https://scholar.google.com/citations?user=VuTRUg8AAAAJ' target='_blank'>Xinyue Li</a><sup>1</sup> 
    <a href='https://scholar.google.com/citations?user=5SuBWh0AAAAJ' target='_blank'>Yating Wang</a><sup>1</sup> 
    <a href='https://www.haoyizhu.site/' target='_blank'>Haoyi Zhu</a><sup>1</sup> 
    <a href='https://mingyulau.github.io/' target='_blank'>Mingyu Liu</a><sup>1,2</sup> 
    <a href='https://scholar.google.com/citations?user=FbSpETgAAAAJ' target='_blank'>Dingning Liu</a><sup>1</sup> 
    <a href='https://yangjiangeyjg.github.io/' target='_blank'>Jiange Yang</a><sup>1</sup>
    <a href='https://github.com/Kr1sJFU' target='_blank'>Zhoujie Fu</a><sup>1</sup>  
    
</div>
<div align='center'>
    <a href='https://sotamak1r.github.io/' target='_blank'>Junyi Chen</a><sup>1</sup> 
    <a href='https://cshen.github.io' target='_blank'>Chunhua Shen</a><sup>2</sup> 
    <a href='https://oceanpang.github.io' target='_blank'>Jiangmiao Pang</a><sup>1</sup> 
    <a href='https://kpzhang93.github.io/' target='_blank'>Kaipeng Zhang</a><sup>1</sup>
    <a href='https://tonghe90.github.io/' target='_blank'>Tong He</a><sup>1†</sup>
</div>
<div align='center'>
    <sup>1</sup>Shanghai AI Lab  <sup>2</sup>ZJU 
</div>
<br>
<div align="center">
  <a href="https://yangzhou24.github.io/OmniWorld/"><img src="https://img.shields.io/badge/Project Page-5745BB?logo=google-chrome&logoColor=white"></a>  
  <a href="https://arxiv.org/abs/2509.12201"><img src="https://img.shields.io/static/v1?label=Paper&message=Arxiv&color=red&logo=arxiv"></a>  
  <a href="https://github.com/yangzhou24/OmniWorld"><img src="https://img.shields.io/static/v1?label=Code&message=Github&color=blue&logo=github"></a>  
  <a href="https://huggingface.co/datasets/InternRobotics/OmniWorld"><img src="https://img.shields.io/static/v1?label=Dataset&message=HuggingFace&color=yellow&logo=huggingface"></a>  
</div>

<img src="assets/teaser.png" width="1000px">

## 🎉 NEWS
- [2025.9.28] The **OmniWorld-CityWalk** dataset is now live on Hugging Face!
- [2025.9.21] 🔥 The **OmniWorld-Game** dataset now includes **5k splits** in total on Hugging Face!
- [2025.9.16] 🔥 The first 1.2k splits release of **OmniWorld-Game** is now live on Hugging Face! **More data is coming soon, stay tuned!**

## 📝 Open-Source Plan

OmniWorld is a multi-domain and multi-modal dataset comprising several distinct sub-datasets. 🙂: The modality is newly (re-)annotated by us, ✅: Ground-truth data that already exists in the original dataset, ❌: Missing modalities.
`✅ Released`: The sub-dataset is publicly available. `🔜 Planned`: The sub-dataset is on our roadmap for a future release. `Full`: The entire sub-dataset is released and available for download. `Partial`: A specified subset of the data is released (e.g., 5k / 96k sequences). `Closed`: The data is not yet publicly available.

| Dataset | Domain | # Seq. | FPS | Resolution | # Frames | Depth | Camera | Text | Opt. flow | Fg. masks | Status | Availability |
| :-- | :-- | --: | --: | :--: | --: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| OmniWorld-Game | Simulator | 96K | 24 | 1280 × 720 | 18,515K | 🙂 | 🙂 | 🙂 | 🙂 | 🙂 | ✅ Released | Partial (5k / 96k) |
| AgiBot | Robot | 20K | 30 | 640 × 480 | 39,247K | 🙂 | ✅ | ✅ | ❌ | 🙂 | 🔜 Planned | Closed  |
| DROID | Robot | 35K | 60 | 1280 × 720 | 26,643K | 🙂 | ✅ | 🙂 | 🙂 | 🙂 | 🔜 Planned | Closed  |
| RH20T | Robot | 109K | 10 | 640 × 360 | 53,453K | ❌ | ✅ | 🙂 | 🙂 | 🙂 | 🔜 Planned | Closed  |
| RH20T-Human | Human | 73K | 10 | 640 × 360 | 8,875K | ❌ | ✅ | 🙂 | ❌ | ❌ | 🔜 Planned | Closed  |
| HOI4D | Human | 2K | 15 | 1920 × 1080 | 891K | 🙂 | 🙂 | 🙂 | 🙂 | ✅ | 🔜 Planned | Closed  |
| Epic-Kitchens | Human | 15K | 30 | 1280 × 720 | 3,635K | ❌ | 🙂 | 🙂 | ❌ | ❌ | 🔜 Planned | Closed  |
| Ego-Exo4D | Human | 4K | 30 | 1024 × 1024 | 9,190K | ❌ | ✅ | 🙂 | 🙂 | ❌ | 🔜 Planned | Closed  |
| HoloAssist | Human | 1K | 30 | 896 × 504 | 13,037K | ❌ | 🙂 | 🙂 | 🙂 | ❌ | 🔜 Planned | Closed  |
| Assembly101 | Human | 4K | 60 | 1920 × 1080 | 110,831K | ❌ | ✅ | 🙂 | 🙂 | 🙂 | 🔜 Planned | Closed  |
| EgoDex | Human | 242K | 30 | 1920 × 1080 | 76,631K | ❌ | ✅ | 🙂 | ❌ | ❌ | 🔜 Planned | Closed  |
| CityWalk | Internet | 7 K | 30 | 1280 × 720 | 13,096K | ❌ | 🙂 | ✅ | ❌ | ❌ | ✅ Released | Full |
---

We will refresh this table whenever a milestone is reached. Your feedback and pull-requests are welcome!

## ✨ Overview

OmniWorld is a large-scale, multi-domain, and multi-modal dataset specifically designed for 🌍**4D world modeling**, e.g. 4D geometric reconstruction, future prediction & camera-controlled video generation.

### 🔑 Key Features

- 📊 **Massive Scale**: 4000+ hours, 600K+ sequences, 300M+ frames
- 🤖 **Diverse Domains**: sourced from simulartor, robot, human & the Internet
- 🎨 **Rich Multi-Modality**: depth maps, camera poses, text captions, optical flow & foreground mask

### 🎮 Introducing _OmniWorld-Game_

_OmniWorld-Game_ is a newly collected high-quality synthetic subset of the main _OmniWorld_ dataset. It features:

- 📊 **Scale**: 214 hours, 96K video clips, 18M+ frames
- 🧩 **Resolution & Diversity**: 720P RGB image capatured from a wide range of dynamic game environments
- 🎨 **Comprehensive Annotations**: cover all annotation types of the _OmniWorld_ dataset

### 🏆 _OmniWorld-Game_ Benchmark

_OmniWorld-Game_ Benchmark offers 4D world modeling evaluation for 3D Geometric Prediction &
Camera Control Video Generation. Found: 

- 🚫 Current state-of-the-art approaches **still show great limitations** in modeling complex 4D environments, based on both quantitative metrics and qualitative results.
- 📈 **Fine-tuning** existing SOTA methods on _OmniWorld_ leads to **significant performance gains** across 4D reconstruction and video generation tasks, highlighting the value of our dataset.


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

> For detailed usage, please refer to [OmniWorld Hugging Face](https://huggingface.co/datasets/InternRobotics/OmniWorld)

## 🚀 Visualize as Point Cloud

This script allows you to convert a scene from OmniWorld-Game dataset into a 3D point cloud for inspection.

### 1\. Prerequisites

Please follow the instructions in the "Dataset Download" section to acquire the OmniWorld-Game dataset.

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

## Citation
If you found this dataset useful, please cite our paper
```bibtex
@misc{zhou2025omniworld,
      title={OmniWorld: A Multi-Domain and Multi-Modal Dataset for 4D World Modeling}, 
      author={Yang Zhou and Yifan Wang and Jianjun Zhou and Wenzheng Chang and Haoyu Guo and Zizun Li and Kaijing Ma and Xinyue Li and Yating Wang and Haoyi Zhu and Mingyu Liu and Dingning Liu and Jiange Yang and Zhoujie Fu and Junyi Chen and Chunhua Shen and Jiangmiao Pang and Kaipeng Zhang and Tong He},
      year={2025},
      eprint={2509.12201},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2509.12201}, 
}
```
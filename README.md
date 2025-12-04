<h1 align='center'>OmniWorld: A Multi-Domain and Multi-Modal Dataset for 4D World Modeling</h1>

<div align="center">
  <a href="https://yangzhou24.github.io/OmniWorld/"><img src="https://img.shields.io/badge/Project Page-5745BB?logo=google-chrome&logoColor=white"></a>  
  <a href="https://arxiv.org/abs/2509.12201"><img src="https://img.shields.io/static/v1?label=Paper&message=Arxiv&color=red&logo=arxiv"></a>  
  <a href="https://github.com/yangzhou24/OmniWorld"><img src="https://img.shields.io/static/v1?label=Code&message=Github&color=blue&logo=github"></a>  
  <a href="https://huggingface.co/datasets/InternRobotics/OmniWorld"><img src="https://img.shields.io/static/v1?label=Dataset&message=HuggingFace&color=yellow&logo=huggingface"></a>  
  <a href="https://modelscope.cn/datasets/InternRobotics/OmniWorld"><img src="https://img.shields.io/static/v1?label=Dataset&message=ModelScope&color=purple&logo=ModelScope"></a>
</div>
<br>
<img src="assets/teaser.png" width="1000px">

## 🎉 NEWS
- [2025.11.11] The **OmniWorld** is now live on 🤖 ModelScope!
- [2025.10.15] 🔥 The **OmniWorld-Game Benchmark** is now live on Hugging Face!
- [2025.10.8] The **OmniWorld-HOI4D** and **OmniWorld-DROID** dataset is now live on Hugging Face!
- [2025.9.28] The **OmniWorld-CityWalk** dataset is now live on Hugging Face!
- [2025.9.21] 🔥 The **OmniWorld-Game** dataset now includes **5k splits** in total on Hugging Face!
- [2025.9.17] 🎉 Our dataset was ranked **#1 Paper of the Day** on 🤗 [Hugging Face Daily Papers](https://huggingface.co/papers/2509.12201)!
- [2025.9.16] 🔥 The first 1.2k splits release of **OmniWorld-Game** is now live on Hugging Face! **More data is coming soon, stay tuned!**

## 📝 Open-Source Plan
| Dataset | Status | Availability | Domain | # Seq. | FPS | Resolution | # Frames | Depth | Camera | Text | Opt. flow | Fg. masks |
| :-- | :-- | --: | --: | :--: | --: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| OmniWorld-Game | ✅ Released | Partial (5k / 96k) | Simulator | 96K | 24 | 1280 × 720 | 18,515K | 🙂 | 🙂 | 🙂 | 🙂 | 🙂 |
| AgiBot | 🔜 Planned | -  | Robot | 20K | 30 | 640 × 480 | 39,247K | 🙂 | ✅ | ✅ | ❌ | 🙂 |
| DROID | ✅ Released | Full  | Robot | 35K | 60 | 1280 × 720 | 26,643K | 🙂 | ✅ | 🙂 | 🙂 | 🙂 |
| RH20T | 🔜 Planned | -  | Robot | 109K | 10 | 640 × 360 | 53,453K | ❌ | ✅ | 🙂 | 🙂 | 🙂 |
| RH20T-Human | 🔜 Planned | -  | Human | 73K | 10 | 640 × 360 | 8,875K | ❌ | ✅ | 🙂 | ❌ | ❌ |
| HOI4D | ✅ Released | Full  | Human | 2K | 15 | 1920 × 1080 | 891K | 🙂 | 🙂 | 🙂 | 🙂 | ✅ |
| Epic-Kitchens | 🔜 Planned | -  | Human | 15K | 30 | 1280 × 720 | 3,635K | ❌ | 🙂 | 🙂 | ❌ | ❌ |
| Ego-Exo4D | 🔜 Planned | -  | Human | 4K | 30 | 1024 × 1024 | 9,190K | ❌ | ✅ | 🙂 | 🙂 | ❌ |
| HoloAssist | 🔜 Planned | -  | Human | 1K | 30 | 896 × 504 | 13,037K | ❌ | 🙂 | 🙂 | 🙂 | ❌ |
| Assembly101 | 🔜 Planned | -  | Human | 4K | 60 | 1920 × 1080 | 110,831K | ❌ | ✅ | 🙂 | 🙂 | 🙂 |
| EgoDex | 🔜 Planned | -  | Human | 242K | 30 | 1920 × 1080 | 76,631K | ❌ | ✅ | 🙂 | ❌ | ❌ |
| CityWalk | ✅ Released | Full | Internet | 7K | 30 | 1280 × 720 | 13,096K | ❌ | 🙂 | ✅ | ❌ | ❌ |
| Game-Benchmark | ✅ Released | Full | Simulator | - | 24 | 1280 × 720 | - | 🙂 | 🙂 | 🙂 | 🙂 | 🙂 |
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

## 🏁 Awesome Works using OmniWorld Dataset

[Depth Anything 3](https://github.com/ByteDance-Seed/Depth-Anything-3): Recovering the Visual Space from Any Views ![GitHub Repo stars](https://img.shields.io/github/stars/ByteDance-Seed/Depth-Anything-3)

[<em>&pi;³</em>](https://github.com/yyfz/Pi3): Permutation-Equivariant Visual Geometry Learning ![GitHub Repo stars](https://img.shields.io/github/stars/yyfz/Pi3)

[Aether](https://github.com/InternRobotics/Aether): Geometric-Aware Unified World Modeling ![GitHub Repo stars](https://img.shields.io/github/stars/InternRobotics/Aether)

[WinT3R](https://github.com/LiZizun/WinT3R): Window-Based Streaming Reconstruction With Camera Token Pool ![GitHub Repo stars](https://img.shields.io/github/stars/LiZizun/WinT3R)

[DeepVerse](https://github.com/SOTAMak1r/DeepVerse): 4D Autoregressive Video Generation as a World Model ![GitHub Repo stars](https://img.shields.io/github/stars/SOTAMak1r/DeepVerse)

[OmniVGGT](https://github.com/Livioni/OmniVGGT-official): Omni-Modality Driven Visual Geometry Grounded Transformer ![GitHub Repo stars](https://img.shields.io/github/stars/Livioni/OmniVGGT-official)

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
If you find this dataset useful, please cite our paper
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
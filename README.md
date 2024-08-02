
# 图像距离图处理和评估
本仓库提供了一些工具，用于处理图像以计算距离图，并评估距离测量范围（DMR）和距离测量精度（DMP）。代码组织在三个主要的 Python 文件中：`image_processing.py`、`evaluation.py` 和 `main.py`。

## 依赖库
确保安装以下 Python 库：

- `opencv-python`
- `numpy`

## 文件结构

- `image_processing.py`：包含读取图像、分离 RGB 通道、计算距离图和从目录中获取图像文件的函数。
- `evaluation.py`：包含计算距离测量范围（DMR）和距离测量精度（DMP）的函数。
- `main.py`：集成图像处理和评估功能的主脚本。

## 使用说明

1. **下载代码**

2. **设置数据集**

   确保数据集的组织结构如下：
   
   ```
   dataset/
   ├── train/
   │   ├── raw_data/
   │   │   ├── 000001.png
   │   │   ├── 000002.png
   │   │   └── ...
   │   ├── groundtruth/
   │       ├── 000001.png
   │       ├── 000002.png
   │       └── ...
   ├── val/
       ├── raw_data/
       │   ├── 000001.png
       │   ├── 000002.png
       │   └── ...
       ├── groundtruth/
           ├── 000001.png
           ├── 000002.png
           └── ...
   ```

3. **编辑 `main.py` 文件**

   在 `main.py` 文件中调整数据集的路径：

   ```python
   train_raw_dir = 'D:\\works\\dataset\\train\\raw_data'
   train_gt_dir = 'D:\\works\\dataset\\train\\groundtruth'
   val_raw_dir = 'D:\\works\\dataset\\val\\raw_data'
   val_gt_dir = 'D:\\works\\dataset\\val\\groundtruth'
   ```

   你还可以通过修改 `image_limit` 变量设置要处理的图像数量：

   ```python
   image_limit = 10  # 修改此值以处理不同数量的图像
   ```

4. **运行主脚本**

   执行主脚本以处理图像并评估结果：

   ```sh
   python main.py
   ```

## 函数详细描述

### `image_processing.py`

- **image_read(image_path)**：从指定路径读取图像。
- **split_channels(rgb_image)**：将 RGB 图像分离为 R、G 和 B 通道。
- **compute_distance_map(R, G, B)**：从 R、G 和 B 通道计算距离图。
- **get_image_files_from_directory(directory, limit=None)**：从目录中获取图像文件路径，可选限制图像数量。

### `evaluation.py`

- **calculate_dmr(distance_map)**：从距离图计算距离测量范围（DMR）。
- **calculate_dmp(predicted_distance_map, ground_truth_distance_map)**：通过比较预测距离图和真实距离图计算距离测量精度（DMP）。

### `main.py`

集成图像处理和评估功能：

- **process_images(image_paths)**：处理一系列图像路径以计算距离图。
- **main()**：主函数，设置目录、处理图像并打印评估指标。

## 注意事项

- 确保图像文件为 `.png` 格式。
- 在 `main.py` 中指定的路径应为包含图像的目录的绝对路径。
- 当前假设真实值和原始数据图像具有 1:1 的对应关系，并在各目录中具有相同的命名。

请根据具体数据集和需求修改路径和参数。

# main.py

import cv2
import numpy as np
from image_processing import image_read, split_channels, compute_distance_map, get_image_files_from_directory
from evaluation import calculate_dmr, calculate_dmp


def process_images(image_paths):
    distance_maps = []
    for image_path in image_paths:
        rgb_image = image_read(image_path)
        R, G, B = split_channels(rgb_image)
        distance_map = compute_distance_map(R, G, B)
        distance_maps.append(distance_map)
    return distance_maps


def main():
    # 训练集和验证集图像路径
    train_raw_dir = 'D:\\works\\dataset\\train\\raw_data'
    train_gt_dir = 'D:\\works\\dataset\\train\\groundtruth'
    val_raw_dir = 'D:\\works\\dataset\\val\\raw_data'
    val_gt_dir = 'D:\\works\\dataset\\val\\groundtruth'

    # 读取图像文件路径（可设置读取图片的数量限制，如限制为10张）
    image_limit = 10
    train_raw_images = get_image_files_from_directory(train_raw_dir, limit=image_limit)
    train_gt_images = get_image_files_from_directory(train_gt_dir, limit=image_limit)
    val_raw_images = get_image_files_from_directory(val_raw_dir, limit=image_limit)
    val_gt_images = get_image_files_from_directory(val_gt_dir, limit=image_limit)

    # 处理训练集图像
    train_distance_maps = process_images(train_raw_images)
    for distance_map in train_distance_maps:
        dmr_min, dmr_max = calculate_dmr(distance_map)
        print(f"训练集测距范围（DMR）：{dmr_min} - {dmr_max}")

    # 处理验证集图像并评估测距精度
    val_pred_distance_maps = process_images(val_raw_images)
    val_gt_distance_maps = process_images(val_gt_images)

    for pred_map, gt_map in zip(val_pred_distance_maps, val_gt_distance_maps):
        dmp = calculate_dmp(pred_map, gt_map)
        print(f"测距精度（DMP）：{dmp}")


if __name__ == "__main__":
    main()
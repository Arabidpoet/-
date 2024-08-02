# image_processing.py

import cv2
import numpy as np
import os

def image_read(image_path):
    """
    读取图像文件
    :param image_path: 图像文件路径
    :return: RGB图像
    """
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    return image

def split_channels(rgb_image):
    """
    分离RGB图像的各个通道
    :param rgb_image: RGB图像
    :return: R, G, B三个通道
    """
    R, G, B = cv2.split(rgb_image)
    return R, G, B

def compute_distance_map(R, G, B):
    """
    计算距离图
    :param R: 红色通道
    :param G: 绿色通道
    :param B: 蓝色通道
    :return: 距离图
    """
    distance_map = ((R.astype(np.uint32) << 16) | (G.astype(np.uint32) << 8) | B.astype(np.uint32))
    return distance_map

def get_image_files_from_directory(directory, limit=None):
    """
    获取目录中的图像文件
    :param directory: 目录路径
    :param limit: 读取图片的数量限制
    :return: 图像文件路径列表
    """
    image_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.png')]
    if limit:
        image_files = image_files[:limit]
    return image_files
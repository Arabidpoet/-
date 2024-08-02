# evaluation.py

import numpy as np

def calculate_dmr(distance_map):
    """
    计算测距范围（DMR）
    :param distance_map: 距离图
    :return: 测距范围
    """
    return np.min(distance_map), np.max(distance_map)

def calculate_dmp(predicted_distance_map, ground_truth_distance_map):
    """
    计算测距精度（DMP）
    :param predicted_distance_map: 预测的距离图
    :param ground_truth_distance_map: 真实距离图
    :return: 测距精度
    """
    abs_diff = np.abs(predicted_distance_map.astype(np.float32) - ground_truth_distance_map.astype(np.float32))
    return np.mean(abs_diff)
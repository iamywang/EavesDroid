# =============================================================================
# This file is part of EavesDroid.
#
# Author: iamywang
# Date Created: Jan 27, 2024
# =============================================================================
import numpy as np
import cydtw
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from backend.backend.view import *

# =============================================================================
# Train and Classify
# =============================================================================
def data_import_interval(path, num_features, num_timestamps, num_interval):
    """
    Import data from .csv file.

    Args:
        path: path to .csv file
        num_features: number of features
        num_timestamps: number of timestamps

    Returns:
        d_sets_scaled: scaled data
        d_labels: labels 
    """
    flist = os.listdir(path)
    nums = len(flist)
    d_sets = np.zeros([nums, num_timestamps, num_features], int)
    d_sets_scaled = np.zeros(
        [nums, int(num_timestamps/num_interval), num_features], np.double)
    d_labels = np.zeros([nums], int)
    for i in range(nums):
        fpath = flist[i]
        label = int(fpath.split('_')[0])
        d_labels[i] = label
        for j in range(num_features):
            d_sets[i, :, j] = np.loadtxt(
                path + fpath, delimiter=',', usecols=j)
    for i in range(num_features):
        for j in range(nums):
            for k in range(int(num_timestamps/num_interval)):
                d_sets_scaled[j, k, i] = d_sets[j, int(k/num_interval), i]
    for i in range(num_features):
        for j in range(nums):
            if (np.max(d_sets_scaled[j, :, i]) - np.min(d_sets_scaled[j, :, i])):
                d_sets_scaled[j, :, i] = (d_sets_scaled[j, :, i] - np.min(d_sets_scaled[j, :, i])) / \
                    (np.max(d_sets_scaled[j, :, i]) -
                     np.min(d_sets_scaled[j, :, i]))
            else:
                d_sets_scaled[j, :, i] = 1
    return d_sets_scaled, d_labels


def predict(K, train_data, train_labels, test_data, test_labels):
    i = 0
    accuracy = 0
    predict_labels = []
    for test in test_data:
        t_dis = []
        for train in train_data:
            dis = cydtw.dtw(test.T, train.T)
            t_dis.append(dis)
        nearest_series_labels = np.array(
            train_labels[np.argpartition(t_dis, K)[:K]]).astype(int)
        preditc_labels_single = np.argmax(np.bincount(nearest_series_labels))
        predict_labels.append(preditc_labels_single)
        if preditc_labels_single == test_labels[i]:
            accuracy += 1
        i += 1
    print('The accuracy is %f (%d of %d)' %
          ((accuracy/test_data.shape[0]), accuracy, test_data.shape[0]))
    return accuracy/test_data.shape[0]


def train_and_classify():
    paths = ['data/OPPO OPPO PGJM10/12 31/train/']

    num_timestamps = 5000
    num_features = 5
    num_interval = 1

    train_sets, train_labels = data_import_interval(
        paths[0], num_features, num_timestamps, num_interval)

    slice_idx = int(len(train_sets) * 0.7)
    test_sets = train_sets[slice_idx:]
    test_labels = train_labels[slice_idx:]
    test_labels = train_labels[slice_idx:]
    train_sets = train_sets[:slice_idx]
    train_labels = train_labels[:slice_idx]

    # test_sets, test_labels = data_import_interval(paths[1], num_features, num_timestamps, num_interval)
    predict(5, train_sets, train_labels, test_sets, test_labels)

train_and_classify()

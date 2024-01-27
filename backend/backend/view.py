# =============================================================================
# This file is part of EavesDroid.
#
# Author: iamywang
# Date Created: Jan 27, 2024
# =============================================================================
import json
import os
from django.http import HttpResponse

import numpy as np
from keras import layers, models


# ================================================================
# data utils
# ================================================================
def data_import(path, num_features, num_timestamps):
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
    d_labels = np.zeros([nums], int)
    for i in range(nums):
        fpath = flist[i]
        label = int(fpath.split('_')[0])
        d_labels[i] = label
        for j in range(num_features):
            d_sets[i, :, j] = np.loadtxt(
                path + fpath, delimiter=',', usecols=j)
    d_sets_scaled = np.zeros([nums, num_timestamps, num_features], np.double)
    for i in range(num_features):
        for j in range(nums):
            d_sets_scaled[j, :, i] = (d_sets[j, :, i] - np.min(d_sets[j, :, i])) / \
                (np.max(d_sets[j, :, i]) - np.min(d_sets[j, :, i]))
    return d_sets_scaled, d_labels


def data_scaled(d_sets, num_features, num_timestamps):
    """
    Scale data with min-max normalization.

    Args:
        d_sets: data
        num_features: number of features
        num_timestamps: number of timestamps

    Returns:
        d_sets_scaled: scaled data
    """
    d_sets_scaled = np.zeros([1, num_timestamps, num_features], np.double)
    for i in range(num_features):
        for j in range(1):
            d_sets_scaled[j, :, i] = (d_sets[j, :, i] - np.min(d_sets[j, :, i])) / \
                (np.max(d_sets[j, :, i]) - np.min(d_sets[j, :, i]))
    return d_sets_scaled


def data_set_label(num_groups, num_features):
    """
    Set labels for data set.

    Args:
        num_groups: number of data in each group
        num_features: number of features

    Returns:
        none
    """
    path = 'test/'
    flist = os.listdir(path)
    nums = len(flist)
    for i in range(nums):
        fpath = flist[i]
        index = int(fpath.split('.')[0])
        label = int(index / num_groups) * num_features + index % num_features
        os.rename(path + fpath, path + str(label) + '_' + fpath)


def cnn_init(model, input_size, num_dims, num_classes):
    """
    Initialize CNN model.

    Args:
        model: keras model
        input_size: number of timestamps
        num_dims: number of features
        num_classes: number of classes

    Returns:
        model: keras model
    """
    model.add(layers.Reshape((int(input_size / 10), num_dims * 10), input_shape=(input_size, num_dims)))

    # conv_1
    model.add(layers.Conv1D(64, 3, activation='leaky_relu'))
    model.add(layers.MaxPooling1D(2))
    model.add(layers.BatchNormalization())

    model.add(layers.Conv1D(128, 3, activation='leaky_relu'))
    model.add(layers.MaxPooling1D(2))
    model.add(layers.BatchNormalization())

    model.add(layers.Conv1D(256, 3, activation='leaky_relu'))
    model.add(layers.MaxPooling1D(2))
    model.add(layers.BatchNormalization())

    # GRU
    model.add(layers.GRU(128, return_sequences=True))
    model.add(layers.BatchNormalization())

    # Flatten
    model.add(layers.Flatten())

    # Output
    model.add(layers.Dense(num_classes, activation='softmax'))
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    print(model.summary())

    return model


# ================================================================
# apis
# ================================================================
def train_model(request):
    """
    Train model.

    Args:
        request: request

    Returns:
        response: response
    """
    num_timestamps = 5000
    num_features = 5
    num_classes = 4
    num_epochs = 100
    num_batch_size = 32

    if request.method == 'POST':
        data = json.loads(request.body)
        device_model = data['model']
        device_version = data['version']
        print('device_model:', device_model)
        print('device_version:', device_version)

        target_dir = 'data/' + device_model + '/' + device_version + '/'
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        if not os.path.exists(target_dir + 'train/'):
            os.makedirs(target_dir + 'train/')
        if not os.path.exists(target_dir + 'test/'):
            os.makedirs(target_dir + 'test/')

        train_sets, train_labels = data_import(
            target_dir + 'train/', num_features, num_timestamps)
        slice_idx = int(len(train_sets) * 0.7)
        test_sets = train_sets[slice_idx:]
        test_labels = train_labels[slice_idx:]
        train_sets = train_sets[:slice_idx]
        train_labels = train_labels[:slice_idx]

        model = models.Sequential()
        model = cnn_init(model, num_timestamps, num_features, num_classes)
        model.fit(train_sets, train_labels, epochs=num_epochs,
                  batch_size=num_batch_size, validation_data=(test_sets, test_labels))
        model.save(target_dir + 'model.h5')

        return HttpResponse('OK')


def save_data(request):
    """
    Save data.

    Args:
        request: request

    Returns:
        response: response
    """
    num_timestamps = 5000
    num_features = 5

    if request.method == 'POST':
        data = json.loads(request.body)
        device_model = data['model']
        device_version = data['version']
        vs1 = data['vs1'].split(',')
        vs2 = data['vs2'].split(',')
        vs3 = data['vs3'].split(',')
        vs4 = data['vs4'].split(',')
        vs5 = data['vs5'].split(',')
        # vs6 = data['vs6'].split(',')
        # vs7 = data['vs7'].split(',')
        # nums = data['nums']
        if len(vs1) < num_timestamps:
            for i in range(0, num_timestamps - len(vs1)):
                vs1.append(vs1[-1])
                vs2.append(vs2[-1])
                vs3.append(vs3[-1])
                vs4.append(vs4[-1])
                vs5.append(vs5[-1])
                # vs6.append(vs6[-1])
                # vs7.append(vs7[-1])

        target_dir = 'data/' + device_model + '/' + device_version + '/'
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        if not os.path.exists(target_dir + 'train/'):
            os.makedirs(target_dir + 'train/')
        if not os.path.exists(target_dir + 'test/'):
            os.makedirs(target_dir + 'test/')

        nums = len(os.listdir(target_dir + 'test/'))
        with open(target_dir + 'test/' + str(nums) + '.txt', 'w') as f:
            for t in range(num_timestamps):
                f.write(vs1[t])
                f.write(',' + vs2[t])
                f.write(',' + vs3[t])
                f.write(',' + vs4[t])
                f.write(',' + vs5[t])
                # f.write(',' + vs6[t])
                # f.write(',' + vs7[t])
                f.write('\n')
        f.close()

        return HttpResponse('OK')

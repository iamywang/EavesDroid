# =============================================================================
# This file is part of EavesDroid.
#
# Author: iamywang
# Date Created: Jan 27, 2024
# =============================================================================
import os
import random
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from keras import models
from backend.backend.view import *
from all_models import *


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
    d_sets_scaled = np.zeros([nums, int(num_timestamps/num_interval), num_features], np.double)
    d_labels = np.zeros([nums], int)
    for i in range(nums):
        fpath = flist[i]
        label = int(fpath.split('_')[0])
        d_labels[i] = label
        for j in range(num_features):
            try:
                d_sets[i, :, j] = np.loadtxt(path + fpath, delimiter=',', usecols=j)
            except:
                print(path + fpath)
    for i in range(num_features):
        for j in range(nums):
            for k in range(int(num_timestamps/num_interval)):
                d_sets_scaled[j, k, i] = d_sets[j, int(k/num_interval), i]
    for i in range(num_features):
        for j in range(nums):
            # # min-max normalization
            if (np.max(d_sets_scaled[j, :, i]) - np.min(d_sets_scaled[j, :, i])):
                d_sets_scaled[j, :, i] = (d_sets_scaled[j, :, i] - np.min(d_sets_scaled[j, :, i])) / \
                    (np.max(d_sets_scaled[j, :, i]) - np.min(d_sets_scaled[j, :, i]))
            else:
                d_sets_scaled[j, :, i] = 1
            
            # z-score normalization
            # if (np.std(d_sets_scaled[j, :, i])):
            #     d_sets_scaled[j, :, i] = (d_sets_scaled[j, :, i] - np.mean(d_sets_scaled[j, :, i])) / \
            #     np.std(d_sets_scaled[j, :, i])
            # else:
            #     d_sets_scaled[j, :, i] = 1

            # mean subtraction
            # d_sets_scaled[j, :, i] = d_sets_scaled[j, :, i] - np.mean(d_sets_scaled[j, :, i])

            # min normalization
            # if (np.max(d_sets_scaled[j, :, i]) - np.min(d_sets_scaled[j, :, i])):
            #     d_sets_scaled[j, :, i] = (d_sets_scaled[j, :, i] - np.mean(d_sets_scaled[j, :, i])) / \
            #         (np.max(d_sets_scaled[j, :, i]) - np.min(d_sets_scaled[j, :, i]))
            # else:
            #     d_sets_scaled[j, :, i] = 1


    return d_sets_scaled, d_labels


def data_import_raw(path, num_features, num_timestamps, num_interval):
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
            d_sets[i, :, j] = np.loadtxt(path + fpath, delimiter=',', usecols=j)
    return d_sets, d_labels


def train_and_save():
    paths = ['data/exp4-complex/noise/0/',
             'data/exp4-complex/noise/1/',
             'data/exp4-complex/noise/2/',
             'data/exp4-complex/noise/3/',
             ]

    num_timestamps = 5000
    num_features = 5
    num_classes = 17
    num_epochs = 100
    num_batch_size = 32
    num_interval = 1

    # import
    train_sets0, train_labels0 = data_import_interval(paths[0], num_features, num_timestamps, num_interval)
    train_sets1, train_labels1 = data_import_interval(paths[1], num_features, num_timestamps, num_interval)
    train_sets2, train_labels2 = data_import_interval(paths[2], num_features, num_timestamps, num_interval)
    train_sets3, train_labels3 = data_import_interval(paths[3], num_features, num_timestamps, num_interval)

    # shuffle
    index = [i for i in range(len(train_labels0))]
    random.shuffle(index)
    train_sets0 = train_sets0[index]
    train_labels0 = train_labels0[index]
    train_sets1 = train_sets1[index]
    train_labels1 = train_labels1[index]
    train_sets2 = train_sets2[index]
    train_labels2 = train_labels2[index]
    train_sets3 = train_sets3[index]
    train_labels3 = train_labels3[index]


    slice_idx = int(len(train_sets0) * 0.7)
    test_sets0 = train_sets0[slice_idx:]
    test_labels0 = train_labels0[slice_idx:]
    train_sets0 = train_sets0[:slice_idx]
    train_labels0 = train_labels0[:slice_idx]
    test_sets1 = train_sets1[slice_idx:]
    test_labels1 = train_labels1[slice_idx:]
    train_sets1 = train_sets1[:slice_idx]
    train_labels1 = train_labels1[:slice_idx]
    test_sets2 = train_sets2[slice_idx:]
    test_labels2 = train_labels2[slice_idx:]
    train_sets2 = train_sets2[:slice_idx]
    train_labels2 = train_labels2[:slice_idx]
    test_sets3 = train_sets3[slice_idx:]
    test_labels3 = train_labels3[slice_idx:]
    train_sets3 = train_sets3[:slice_idx]
    train_labels3 = train_labels3[:slice_idx]

    # train_sets = np.concatenate((train_sets0, train_sets1, train_sets2, train_sets3), axis=0)
    # train_labels = np.concatenate((train_labels0, train_labels1, train_labels2, train_labels3), axis=0)
    # test_sets = np.concatenate((test_sets0, test_sets1, test_sets2, test_sets3), axis=0)
    # test_labels = np.concatenate((test_labels0, test_labels1, test_labels2, test_labels3), axis=0)

    # model = models.Sequential()
    # model = cnn_init(model, int(num_timestamps/num_interval), num_features, num_classes)

    # best = 0
    # for i in range(num_epochs):
    #     res = model.fit(train_sets, train_labels, epochs=1, batch_size=num_batch_size, validation_data=(test_sets, test_labels))
    #     if res.history['val_accuracy'][-1] > best:
    #         best = res.history['val_accuracy'][-1]
    #         model.save('data/exp4-complex/models/model_xiaomi9_12_noise2.h5')
    #         print('epoch: %d, best: %f' % (i, best))
        
    model = models.load_model('data/exp4-complex/models/model_xiaomi9_12_noise2.h5')
    
    # for all 0
    # label 0~3
    test_set = test_sets0[test_labels0 < 4]
    test_label = test_labels0[test_labels0 < 4]
    model.evaluate(test_set, test_label)
    # label 4~8
    test_set = test_sets0[test_labels0 > 3]
    test_label = test_labels0[test_labels0 > 3]
    test_set = test_set[test_label < 9]
    test_label = test_label[test_label < 9]
    model.evaluate(test_set, test_label)
    # label 9~12
    test_set = test_sets0[test_labels0 > 8]
    test_label = test_labels0[test_labels0 > 8]
    test_set = test_set[test_label < 13]
    test_label = test_label[test_label < 13]
    model.evaluate(test_set, test_label)
    # label 13~16
    test_set = test_sets0[test_labels0 > 12]
    test_label = test_labels0[test_labels0 > 12]
    model.evaluate(test_set, test_label)
    # label 0~16
    model.evaluate(test_sets0, test_labels0)

    # for all 1
    # label 0~3
    test_set = test_sets1[test_labels1 < 4]
    test_label = test_labels1[test_labels1 < 4]
    model.evaluate(test_set, test_label)
    # label 4~8
    test_set = test_sets1[test_labels1 > 3]
    test_label = test_labels1[test_labels1 > 3]
    test_set = test_set[test_label < 9]
    test_label = test_label[test_label < 9]
    model.evaluate(test_set, test_label)
    # label 9~12
    test_set = test_sets1[test_labels1 > 8]
    test_label = test_labels1[test_labels1 > 8]
    test_set = test_set[test_label < 13]
    test_label = test_label[test_label < 13]
    model.evaluate(test_set, test_label)
    # label 13~16
    test_set = test_sets1[test_labels1 > 12]
    test_label = test_labels1[test_labels1 > 12]
    model.evaluate(test_set, test_label)
    # label 0~16
    model.evaluate(test_sets1, test_labels1)

    # for all 2
    # label 0~3
    test_set = test_sets2[test_labels2 < 4]
    test_label = test_labels2[test_labels2 < 4]
    model.evaluate(test_set, test_label)
    # label 4~8
    test_set = test_sets2[test_labels2 > 3]
    test_label = test_labels2[test_labels2 > 3]
    test_set = test_set[test_label < 9]
    test_label = test_label[test_label < 9]
    model.evaluate(test_set, test_label)
    # label 9~12
    test_set = test_sets2[test_labels2 > 8]
    test_label = test_labels2[test_labels2 > 8]
    test_set = test_set[test_label < 13]
    test_label = test_label[test_label < 13]
    model.evaluate(test_set, test_label)
    # label 13~16
    test_set = test_sets2[test_labels2 > 12]
    test_label = test_labels2[test_labels2 > 12]
    model.evaluate(test_set, test_label)
    # label 0~16
    model.evaluate(test_sets2, test_labels2)

    # for all 3
    # label 0~3
    test_set = test_sets3[test_labels3 < 4]
    test_label = test_labels3[test_labels3 < 4]
    model.evaluate(test_set, test_label)
    # label 4~8
    test_set = test_sets3[test_labels3 > 3]
    test_label = test_labels3[test_labels3 > 3]
    test_set = test_set[test_label < 9]
    test_label = test_label[test_label < 9]
    model.evaluate(test_set, test_label)
    # label 9~12
    test_set = test_sets3[test_labels3 > 8]
    test_label = test_labels3[test_labels3 > 8]
    test_set = test_set[test_label < 13]
    test_label = test_label[test_label < 13]
    model.evaluate(test_set, test_label)
    # label 13~16
    test_set = test_sets3[test_labels3 > 12]
    test_label = test_labels3[test_labels3 > 12]
    model.evaluate(test_set, test_label)
    # label 0~16
    model.evaluate(test_sets3, test_labels3)


def test_and_classify():
    paths = ['data/exp4-complex/sequence/']
    
    num_timestamps = 5000
    num_features = 5
    num_interval = 1

    model = models.load_model('models/model_xiaomi9_12_sequence.h5')

    for i in range(len(paths)):
        test_sets, test_labels = data_import_interval(paths[i], num_features, num_timestamps, num_interval)

        # label 0~16
        test_set = test_sets[test_labels < 17]
        test_label = test_labels[test_labels < 17]
        model.evaluate(test_set, test_label)

        # label 17~28
        test_set = test_sets[test_labels > 16]
        test_label = test_labels[test_labels > 16]
        test_set = test_set[test_label < 29]
        test_label = test_label[test_label < 29]
        model.evaluate(test_set, test_label)

        # label 29~40
        test_set = test_sets[test_labels > 28]
        test_label = test_labels[test_labels > 28]
        model.evaluate(test_set, test_label)

        test_loss, test_acc = model.evaluate(test_sets, test_labels)
        print('test_acc:', test_acc)


def train_1d_cnn():
    paths = ['data/exp1-accuracy_additional_impact/normal/OPPO OPPO PGJM10/']

    num_timestamps = 5000
    num_features = 5
    num_classes = 17
    num_epochs = 100
    num_batch_size = 32
    num_interval = 1

    train_sets, train_labels = data_import_interval(paths[0], num_features, num_timestamps, num_interval)

    # 随机打乱数据
    index = [i for i in range(len(train_labels))]
    random.shuffle(index)
    train_sets = train_sets[index]
    train_labels = train_labels[index]

    slice_idx = int(len(train_sets) * 0.7)
    test_sets = train_sets[slice_idx:]
    test_labels = train_labels[slice_idx:]
    test_labels = train_labels[slice_idx:]
    train_sets = train_sets[:slice_idx]
    train_labels = train_labels[:slice_idx]

    # model = models.Sequential()
    # model = rnn2_init(model, int(num_timestamps/num_interval), num_features, num_classes)

    # best = 0
    # for i in range(num_epochs):
    #     res = model.fit(train_sets, train_labels, epochs=1, batch_size=num_batch_size, validation_data=(test_sets, test_labels))
    #     if res.history['val_accuracy'][-1] > best:
    #         best = res.history['val_accuracy'][-1]
    #         model.save('models/model_oppok10_12_model_gru.h5')
    #         print('epoch: %d, best: %f' % (i, best))
    
    model = models.load_model('models/model_oppok10_12_model_gru.h5')


    # label 0~3
    test_set = test_sets[test_labels < 4]
    test_label = test_labels[test_labels < 4]
    model.evaluate(test_set, test_label)

    # label 4~8
    test_set = test_sets[test_labels > 3]
    test_label = test_labels[test_labels > 3]
    test_set = test_set[test_label < 9]
    test_label = test_label[test_label < 9]
    model.evaluate(test_set, test_label)

    # label 9~12
    test_set = test_sets[test_labels > 8]
    test_label = test_labels[test_labels > 8]
    test_set = test_set[test_label < 13]
    test_label = test_label[test_label < 13]
    model.evaluate(test_set, test_label)

    # label 13~16
    test_set = test_sets[test_labels > 12]
    test_label = test_labels[test_labels > 12]
    model.evaluate(test_set, test_label)

    model.evaluate(test_sets, test_labels)

train_and_save()
# test_and_classify()
# train_1d_cnn()

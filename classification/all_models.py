# =============================================================================
# This file is part of EavesDroid.
#
# Author: iamywang
# Date Created: Jan 27, 2024
# =============================================================================
from keras import layers

def one_dim_cnn_init(model, input_size, num_dims, num_classes):
    model.add(layers.Reshape((int(input_size / 10), num_dims * 10), input_shape=(input_size, num_dims)))

    model.add(layers.Conv1D(100, 10, activation='relu'))
    model.add(layers.Conv1D(100, 10, activation='relu'))
    model.add(layers.MaxPooling1D(3))
    model.add(layers.Conv1D(160, 10, activation='relu'))
    model.add(layers.Conv1D(160, 10, activation='relu'))
    model.add(layers.GlobalAveragePooling1D())
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(num_classes, activation='softmax'))
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    print(model.summary())

    return model

def rnn_init(model, input_size, num_dims, num_classes):
    model.add(layers.LSTM(128, input_shape=(input_size, num_dims), return_sequences=True))
    model.add(layers.LSTM(128, return_sequences=False))
    model.add(layers.Dense(num_classes, activation='softmax'))
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    print(model.summary())

    return model

def rnn2_init(model, input_size, num_dims, num_classes):
    model.add(layers.GRU(128, input_shape=(input_size, num_dims), return_sequences=True))
    model.add(layers.GRU(128, return_sequences=False))
    model.add(layers.Dense(num_classes, activation='softmax'))
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    print(model.summary())

    return model
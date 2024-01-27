# =============================================================================
# This file is part of EavesDroid.
#
# Author: iamywang
# Date Created: Jan 27, 2024
# =============================================================================
from backend.backend.view import *
from keras.utils import plot_model

model = models.Sequential()
model = cnn_init(model, 5000, 3, 4)

plot_model(model, to_file='figures/tab2.eps', show_shapes=True)

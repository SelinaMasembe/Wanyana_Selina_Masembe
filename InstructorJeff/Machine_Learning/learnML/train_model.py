#import required libraries

import os
import numpy as np
import tensorflow as tf #type: ignore    for building and training deep learning models
from tensorflow import keras #type: ignore   high level API for neural networks
from tensorflow.keras.processing.image import ImageDataGenerator #type: ignore   -Augumentation
from tensorflow.keras.models import Sequential #type: ignore   -for building sequential models, linear stack of neural layers
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D, Dropout #type: ignore   -for building layers of the model,layer CNN
from tensorflow.keras.optimizers import Adam #type: ignore   -for optimization algorithms
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint #type: ignore   -for early stopping during training ,Training callbacks
from matplotlib import pyplot as plt     #-for plotting graphs
#import required libraries

import os
import numpy as np

import tensorflow as tf  
#for building and training deep learning models



from tensorflow import keras 
#high level API for neural networks
from tensorflow.keras.preprocessing.image import ImageDataGenerator #type: ignore   
#-Augumentation

from tensorflow.keras.models import Sequential #type: ignore
#-for building sequential models, linear stack of neural layers

from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D, Dropout #type: ignore   
#-for building layers of the model,layer CNN

from tensorflow.keras.optimizers import Adam #type: ignore
#-for optimization algorithmspip install tensorflow


from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint #type: ignore  
#-for early stopping during training ,Training callbacks

from matplotlib import pyplot as plt     #-for plotting graphs


#Set up random seeds for reproducibility

"""
before we train the model, we need to:
1.augment the data
2.shuffle the data
3.split the data into training and validation sets
4.generate random test cases


np.random.seed(42)  # Set seed for NumPy
why 42?
  -it helps to reproduce the experiment. for consistent results across different runs.
 -it is a common practice in machine learning to set a random seed for reproducibility.
 """


#to seed the data
tf.random.set_seed(42)  # Set seed for TensorFlow
np.random.seed(42)  # Set seed for NumPy - for image augumentation (resizing, rotation, etc.)

#after setting that the images should be resized, you can now define the image size

"""
WHY DEFINING A FIXED IMAGE SIZE?
#  -it is a common practice in machine learning to resize images to a fixed size for consistency.
#  -it helps to reduce the computational cost and memory usage.
#  -it is also required by the model to have a fixed input size.
"""



#DEFINING THE COSTANT IMAGE SIZE
IMAGE_SIZE = (256, 256)  # Define the input image size (height, width) to be squares.

#PROCESSING ALL THE IMAGES
BATCH_SIZE = 32  # Define the batch size for number of images to be processed at once.

EPOCHS = 10  # Define the number of full times(32 set each) to pass through the entire dataset during training.

CROP_CLASSES = 2  # Define the number of classes in the dataset (e.g., diseased and healthy). 
ANIMAL_CLASSES = 3  # Define the number of animal classes in the dataset (e.g., cat, dog, human).

#DEFINE DATA SET DIRECTORY AND MODEL SAVE PATHS
DATASET_DIR = "learnML"  # Define the directory where the dataset is stored.-the folder name
MODEL_PATH = "selina_model.h5"  # Define the path where the trained model will be saved.
#.h5 is the file extension for Keras models. it is the most accurate file format for saving Keras models.

#DEEP LEARNING -Convolutional Neural Networks (CNNs) for image classification
# This code is for training a Convolutional Neural Network (CNN) model using TensorFlow and Keras.

#import required libraries
import os
import numpy as np

#for building and training deep learning models
import tensorflow as tf

#keras->high level API for neural networks

#-Augumentation
from tensorflow.keras.preprocessing.image import ImageDataGenerator  # type: ignore

#-for building sequential models, linear stack of neural layers
from tensorflow.keras.models import Sequential  # type: ignore

#-for building layers of the model,layer CNN
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout  # type: ignore

#-for optimization algorithmspip install tensorflow
from tensorflow.keras.optimizers import Adam  # type: ignore

#-for early stopping during training ,Training callbacks
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping  # type: ignore

#-for plotting graphs
import matplotlib.pyplot as plt

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

# Constants
IMAGE_SIZE = (256, 256)  # Define the input image size (height, width) to be squares.
BATCH_SIZE = 32 # Define the batch size for number of images to be processed at once.
EPOCHS = 20 # Define the number of full times(32 set each) to pass through the entire dataset during training.
NUM_CLASSES = 2  # Healthy vs Diseased (for crops)
ANIMAL_CLASSES = 3  # Dog, Cat, Human (for filtering)

# Paths
# Should contain subfolders: crops/healthy, crops/diseased, animals/dog, animals/cat, animals/human
DATASET_DIR = "learmML" # Define the directory where the dataset is stored.-the folder name
MODEL_PATH = "selina_model.h5"  # Define the path where the trained model will be saved.
#.h5 is the file extension for Keras models. it is the most accurate file format for saving Keras models.

"""Create a CNN model for classification"""
def create_model(input_shape, num_classes):
    """
    conv2d - increasing filters for your images e.g brightness
    first variable in con2d -> is num of filters - for clearer images
    once filters are increased, there is need for re-sizing the length and width -USE MAXPOOLING2D
    THEREFORE EVERY CON2D HAS A MAXPOOLING2D
    """
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=input_shape), #filters , 3X3 kernel
        MaxPooling2D(2, 2),
        
        #doubling filters
        Conv2D(64, (3, 3), activation='relu'), #increase to 64 the filter
        MaxPooling2D(2, 2),
        
        Conv2D(128, (3, 3), activation='relu'),#increase filter to 128
        MaxPooling2D(2, 2),
        
        Conv2D(256, (3, 3), activation='relu'), #increase filter to 256
        MaxPooling2D(2, 2),
        
        Flatten(),
        Dropout(0.5),#dropout to 50% of the neurons to prevent overfitting or zooming
        Dense(512, activation='relu'),
        Dense(num_classes, activation='softmax')
    ])
    
    
    #Compiling the model with an optimizer
    model.compile(optimizer=Adam(learning_rate=0.0001),loss='categorical_crossentropy',metrics=['accuracy'])
    return model


def train_crop_model():
    """Train the main crop disease detection model"""
    # Data generators with augmentation
    train_datagen = ImageDataGenerator(
        rescale=1./255, #Normalize pixel values to [0,1] -> The value "1./255 is constant for all rescales"
        rotation_range=40, #for the model to detect all images whatever the rotational angle.
        width_shift_range=0.2, #range if you shift the images horizontally
        height_shift_range=0.2,  # --- vertically
        shear_range=0.2, #transformation
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest',
        validation_split=0.2
    )

    # Load datasets
    train_generator = train_datagen.flow_from_directory(
        os.path.join(DATASET_DIR, "crops"),
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical', #one-hot encoding for labels
        subset='training' #load only the validation subset
    )

    #loading validation images
    validation_generator = train_datagen.flow_from_directory(
        os.path.join(DATASET_DIR, "crops"),
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='validation'
    )

    # Create and train model-a CNN model for each category eg crops
    model = create_model(IMAGE_SIZE + (3,), NUM_CLASSES)

    callbacks = [
        ModelCheckpoint(MODEL_PATH, save_best_only=True), #saves best model with best validation
        EarlyStopping(patience=5, restore_best_weights=True) #stops if no improvement or validation.
    ]

    #train the model on thetraining datasets on validation sets 
    history = model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples // BATCH_SIZE,
        epochs=EPOCHS,
        validation_data=validation_generator,
        validation_steps=validation_generator.samples // BATCH_SIZE,
        callbacks=callbacks
    )

    # Plot training history
    plot_training_history(history)
    return model


def train_animal_filter():
    """Train a secondary model to filter out animals/humans"""
    animal_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

    train_generator = animal_datagen.flow_from_directory(
        os.path.join(DATASET_DIR, "animals"),
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='training'
    )

    validation_generator = animal_datagen.flow_from_directory(
        os.path.join(DATASET_DIR, "animals"),
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='validation'
    )

    model = create_model(IMAGE_SIZE + (3,), ANIMAL_CLASSES)

    model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples // BATCH_SIZE,
        epochs=10,
        validation_data=validation_generator,
        validation_steps=validation_generator.samples // BATCH_SIZE
    )

    return model


def plot_training_history(history):
    """Plot training and validation accuracy/loss"""
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs_range = range(len(acc))

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')

    plt.savefig('training_history.png')
    plt.close()


def predict_image(model, animal_model, image_path):
    """Predict if image is healthy/diseased crop or animal/human"""
    img = tf.keras.preprocessing.image.load_img(
        image_path, target_size=IMAGE_SIZE
    )
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    # First check if it's an animal/human
    animal_pred = animal_model.predict(img_array)
    animal_classes = ['dog', 'cat', 'human']
    animal_prob = np.max(animal_pred)

    if animal_prob > 0.9:  # High confidence it's an animal/human
        return {
            'type': 'animal',
            'class': animal_classes[np.argmax(animal_pred)],
            'confidence': float(animal_prob)
        }

    # If not animal, check for crops
    crop_pred = model.predict(img_array)
    crop_classes = ['healthy', 'diseased']
    return {
        'type': 'crop',
        'class': crop_classes[np.argmax(crop_pred)],
        'confidence': float(np.max(crop_pred))
    }


if __name__ == "__main__":
    # Train or load models
    if not os.path.exists(MODEL_PATH):
        print("Training crop disease model...")
        crop_model = train_crop_model()
        print("Training animal filter model...")
        animal_model = train_animal_filter()
    else:
        print("Loading existing models...")
        crop_model = tf.keras.models.load_model(MODEL_PATH)
        animal_model = create_model(IMAGE_SIZE + (3,), ANIMAL_CLASSES)
        # Note: In production, you should save/load the animal model too

    # Test prediction
    test_image = "test_image.jpg"  # Replace with your test image
    if os.path.exists(test_image):
        prediction = predict_image(crop_model, animal_model, test_image)
        print("\nPrediction Results:")
        print(f"Type: {prediction['type']}")
        print(f"Class: {prediction['class']}")
        print(f"Confidence: {prediction['confidence']:.2%}")
    else:
        print(f"Test image {test_image} not found")

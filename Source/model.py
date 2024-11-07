"""
Developed by Mojtaba Fazli.

This code is provided for researchers and developers interested in leveraging it for their own projects. 
Please make sure to reference this code if you use it in your work or publications.

Description:
This FastAPI application is designed for uploading, processing, and predicting ECG data using a pre-trained model.

Published Date: Nov. 2, 2024
"""

import tensorflow as tf
from tensorflow_addons.optimizers import RectifiedAdam

## Define custom metrics

# Pearson correlation coefficient
def pearson(y_true, y_pred):
    # Calculate Pearson correlation
    x = y_true - tf.reduce_mean(y_true)
    y = y_pred - tf.reduce_mean(y_pred)
    correlation = tf.reduce_sum(x * y) / (tf.sqrt(tf.reduce_sum(tf.square(x))) * tf.sqrt(tf.reduce_sum(tf.square(y))))
    return correlation

# Example custom metric for male_precision
def male_precision(y_true, y_pred):
    return tf.keras.metrics.Precision()(y_true, y_pred)

# Example custom metric for female_precision
def female_precision(y_true, y_pred):
    return tf.keras.metrics.Precision()(y_true, y_pred)

# Example custom metric for female_recall
def female_recall(y_true, y_pred):
    return tf.keras.metrics.Recall()(y_true, y_pred)

# Example custom metric for male_recall
def male_recall(y_true, y_pred):
    return tf.keras.metrics.Recall()(y_true, y_pred)

def atrial_fibrillation_precision(y_true, y_pred):  # Add this function
    return tf.keras.metrics.Precision()(y_true, y_pred)

def atrial_fibrillation_recall(y_true, y_pred):  # Add this function
    return tf.keras.metrics.Recall()(y_true, y_pred)

def no_atrial_fibrillation_precision(y_true, y_pred):
    return tf.keras.metrics.Precision()(y_true, y_pred)  # Example precision function, adjust as needed

def no_atrial_fibrillation_recall(y_true, y_pred):  # Add this function
    return tf.keras.metrics.Recall()(y_true, y_pred)

# Example custom loss function
def custom_loss(y_true, y_pred):
    return tf.reduce_mean(tf.square(y_true - y_pred))  # Example using Mean Squared Error

def load_model():
    MODEL_PATH = "/ECG2AF_WebApp/ml4h/model_zoo/ECG2AF/ecg_5000_survival_curve_af_quadruple_task_mgh_v2021_05_21.h5"

    # Include all custom objects used in the model
    custom_objects = {
        'RectifiedAdam': RectifiedAdam,
        'custom_loss': custom_loss,           # Restored custom_loss here
        'loss': custom_loss,
        'female_precision': female_precision,  # Ensure this is included
        'male_precision': male_precision,
        'male_recall': male_recall,
        'female_recall': female_recall,
        'pearson': pearson,  # Include the pearson metric here
        'no_atrial_fibrillation_precision': no_atrial_fibrillation_precision,  # Include this newly defined metric
        'no_atrial_fibrillation_recall': no_atrial_fibrillation_recall,  # Include this newly defined metric
        'atrial_fibrillation_precision': atrial_fibrillation_precision,  # Include this newly defined metric
        'atrial_fibrillation_recall': atrial_fibrillation_recall,  # Include this newly defined metric


    }

    model = tf.keras.models.load_model(MODEL_PATH, custom_objects=custom_objects)
    return model

"""
Developed by Mojtaba Fazli.

Description:
This module contains the functionality for loading a pre-trained ECG model and making predictions 
based on input data.

Published Date: Nov. 2, 2024
"""

import tensorflow as tf
import numpy as np
import h5py

# Load the pre-trained ECG model
model = tf.keras.models.load_model('path_to_ecg2af_model.h5')

def predict_ecg(file_path):
    """
    Function to predict ECG data using the pre-trained model.

    Args:
        file_path (str): Path to the ECG data file in .h5 format.

    Returns:
        numpy.ndarray or None: The prediction result from the model or None if an error occurs.
    """
    try:
        # Open the .h5 file and load ECG data
        with h5py.File(file_path, 'r') as f:
            ecg_data = np.array(f['ecg'])
        
        # Perform prediction using the model
        return model.predict(ecg_data)
    except Exception as e:
        # Print error message if prediction fails
        print(f"Error in prediction: {e}")
        return None

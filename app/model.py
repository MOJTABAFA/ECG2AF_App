import tensorflow as tf
import numpy as np
import h5py

model = tf.keras.models.load_model('path_to_ecg2af_model.h5')

def predict_ecg(file_path):
    try:
        with h5py.File(file_path, 'r') as f:
            ecg_data = np.array(f['ecg'])
        return model.predict(ecg_data)
    except Exception as e:
        print(f"Error in prediction: {e}")
        return None

import tensorflow as tf
import numpy as np

# Path to the pre-trained model
MODEL_PATH = 'ml4h/model_zoo/ECG2AF/ecg_5000_survival_curve_af_quadruple_task_mgh_v2021_05_21.h5'

def load_model():
    """
    Load the pre-trained ECG2AF model from the specified path.
    Returns:
        tf.keras.Model: The loaded TensorFlow model.
    """
    model = tf.keras.models.load_model(MODEL_PATH)
    return model

def ecg_as_tensor(ecg_data):
    """
    Convert ECG data to a tensor format suitable for the model.
    Args:
        ecg_data (list or np.ndarray): Raw ECG data.
    Returns:
        tf.Tensor: The ECG data as a tensor.
    """
    return tf.convert_to_tensor(ecg_data, dtype=tf.float32)

def predict_ecg(model, tensor):
    """
    Make predictions using the provided model and input tensor.
    Args:
        model (tf.keras.Model): The pre-trained model.
        tensor (np.ndarray): The pre-processed input tensor.
    Returns:
        dict: A dictionary with prediction results.
    """
    predictions = model.predict(tensor)
    results = {
        "Prediction 1": float(predictions[0][0]),
        "Prediction 2": float(predictions[0][1]),
        "Prediction 3": float(predictions[0][2]),
        "Prediction 4": float(predictions[0][3])
    }
    return results

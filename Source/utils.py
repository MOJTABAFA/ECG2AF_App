import h5py
import io
import numpy as np
import tensorflow as tf

# Path to the pre-trained model
MODEL_PATH = '/ECG2AF_WebApp/ml4h/model_zoo/ECG2AF/ecg_5000_survival_curve_af_quadruple_task_mgh_v2021_05_21.h5'

# Define constants for ECG data
ECG_REST_LEADS = {
    'strip_I': 0, 'strip_II': 1, 'strip_III': 2, 'strip_V1': 3, 
    'strip_V2': 4, 'strip_V3': 5, 'strip_V4': 6, 'strip_V5': 7, 
    'strip_V6': 8, 'strip_aVF': 9, 'strip_aVL': 10, 'strip_aVR': 11
}
ECG_SHAPE = (5000, 12)
ECG_HD5_PATH = 'ukb_ecg_rest'

def load_model():
    """
    Load the pre-trained ECG2AF model from the specified path.
    """
    custom_objects = {}  # Add custom metrics or losses if necessary
    model = tf.keras.models.load_model(MODEL_PATH, custom_objects=custom_objects)
    return model

def ecg_as_tensor(file_content):
    """
    Convert the contents of an .hd5 file to a tensor format with the expected shape.
    Args:
        file_content (bytes): Raw file content in .hd5 format.
    Returns:
        tf.Tensor: The ECG data as a tensor with shape (1, 5000, 12).
    """
    with h5py.File(io.BytesIO(file_content), 'r') as hd5:
        tensor = np.zeros(ECG_SHAPE, dtype=np.float32)
        for lead in ECG_REST_LEADS:
            data_path = f"{ECG_HD5_PATH}/{lead}/instance_0"
            if data_path in hd5:
                data = np.array(hd5[data_path])
                tensor[:, ECG_REST_LEADS[lead]] = data
            else:
                raise ValueError(f"Lead {lead} not found in file.")
        
        # Normalize the tensor as per the expected format
        tensor -= np.mean(tensor)
        tensor /= np.std(tensor) + 1e-6

    # Confirm shape before adding the batch dimension
    print(f"Shape before adding batch dimension: {tensor.shape}")  # Expecting (5000, 12)
    
    # Ensure the tensor has the correct shape for model input
    tensor = np.expand_dims(tensor, axis=0)  # Should become (1, 5000, 12)
    print(f"Shape after adding batch dimension: {tensor.shape}")
    
    return tf.convert_to_tensor(tensor, dtype=tf.float32)

def predict_ecg(model, tensor):
    """
    Make predictions using the provided model and input tensor.
    Args:
        model (tf.keras.Model): The pre-trained model.
        tensor (tf.Tensor): The pre-processed input tensor.
    Returns:
        dict: A dictionary with prediction results.
    """
    if not isinstance(tensor, tf.Tensor):
        tensor = tf.convert_to_tensor(tensor, dtype=tf.float32)
    
    # Ensure the tensor has the correct shape for the model
    tensor = tf.reshape(tensor, (1, 5000, 12))  # Explicitly reshape to (1, 5000, 12)
    print(f"Tensor shape before prediction: {tensor.shape}")

    # Make predictions and handle the output
    predictions = model.predict(tensor)
    print(f"Raw predictions output: {predictions}")  # Print raw predictions for debugging

    # Handle complex prediction structure by iterating through each array
    results = {}
    for i, prediction in enumerate(predictions):
        # Check if prediction is a single scalar or an array
        if isinstance(prediction, np.ndarray) and prediction.size > 1:
            # Take only the first few values if it's a larger array
            results[f"Prediction {i + 1}"] = prediction[0][:4].tolist()  # Convert to list for JSON compatibility
        else:
            # Handle single-value outputs
            results[f"Prediction {i + 1}"] = float(prediction) if np.isscalar(prediction) else float(prediction[0])

    return results

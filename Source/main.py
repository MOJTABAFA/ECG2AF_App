# Import necessary libraries from FastAPI and utility modules
from fastapi import FastAPI, File, UploadFile, HTTPException
import numpy as np
from model import load_model
from utils import ecg_as_tensor, predict_ecg
import tensorflow_addons as tfa  # Ensure custom layers are imported

# Initialize FastAPI application
app = FastAPI()

# Load the pre-trained ECG2AF model
model = load_model()  # Load the model from the model.py script

@app.post("/upload/")
async def upload_ecg(file: UploadFile = File(...)):
    """
    Endpoint to upload an ECG file, process it, and return predictions.
    Args:
        file (UploadFile): The uploaded ECG file in .hd5 format.
    Returns:
        dict: A dictionary containing the model's predictions.
    """
    # Validate file format
    if not file.filename.endswith('.hd5'):
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload an .hd5 file.")
    try:
        # Convert the uploaded file to a tensor
        tensor = ecg_as_tensor(file.file)
        tensor = np.expand_dims(tensor, axis=0)  # Add batch dimension for model input

        # Get predictions from the model
        results = predict_ecg(model, tensor)
        return {"results": results}
    except Exception as e:
        # Handle any exceptions during processing
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

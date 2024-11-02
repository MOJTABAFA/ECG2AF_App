"""
Developed by Mojtaba Fazli.

This code is provided for researchers and developers interested in leveraging it for their own projects. Please make sure to reference this code if you use it in your work or publications.

Description:
This FastAPI application is designed for uploading, processing, and predicting ECG data using a pre-trained model.

Published Date: Nov. 2, 2024
"""

from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.model import predict_ecg
from app.utils import save_upload_file, remove_file

# Create FastAPI app instance
app = FastAPI()

# Set up template rendering and static file handling
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def upload_page(request: Request):
    """
    Endpoint to render the upload page.
    """
    return templates.TemplateResponse("upload.html", {"request": request})

@app.post("/upload", response_class=HTMLResponse)
async def handle_file_upload(request: Request, file: UploadFile = File(...)):
    """
    Endpoint to handle file uploads and process the uploaded ECG file.

    Args:
        request (Request): The HTTP request object.
        file (UploadFile): The uploaded file to be processed.

    Returns:
        TemplateResponse: Rendered HTML response with predictions or an error message.
    """
    # Check if the uploaded file has a valid .h5 format
    if not file.filename.endswith(".h5"):
        return templates.TemplateResponse("upload.html", {
            "request": request,
            "error": "Invalid file format. Please upload an HD5 file."
        })

    # Save the uploaded file temporarily
    file_path = save_upload_file(file, Path("uploads"))

    # Run the prediction function
    predictions = predict_ecg(file_path)

    # Remove the uploaded file after processing
    remove_file(file_path)

    # Check if predictions were successfully generated
    if predictions is None:
        return templates.TemplateResponse("upload.html", {
            "request": request,
            "error": "Error processing file. Please try again."
        })

    # Return predictions in the results template
    return templates.TemplateResponse("results.html", {
        "request": request,
        "predictions": predictions
    })

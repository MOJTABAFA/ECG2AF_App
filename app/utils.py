"""
Developed by Mojtaba Fazli.

Description:
This module contains utility functions for handling file operations such as saving uploaded files and removing files.

Published Date: Nov. 2, 2024
"""

import os
from fastapi import UploadFile
from pathlib import Path

# Define the upload folder path
UPLOAD_FOLDER = Path("uploads")

def save_upload_file(upload_file: UploadFile, destination: Path) -> Path:
    """
    Saves an uploaded file to a specified destination.

    Args:
        upload_file (UploadFile): The file to be uploaded.
        destination (Path): The directory where the file will be saved.

    Returns:
        Path: The full path of the saved file.
    """
    file_path = UPLOAD_FOLDER / upload_file.filename
    with file_path.open("wb") as buffer:
        # Write file content to the specified path
        buffer.write(upload_file.file.read())
    return file_path

def remove_file(file_path: Path):
    """
    Removes a file from the filesystem.

    Args:
        file_path (Path): The path to the file to be removed.

    Returns:
        None
    """
    try:
        # Attempt to delete the file
        os.remove(file_path)
    except Exception as e:
        # Print error message if file deletion fails
        print(f"Error deleting file: {e}")

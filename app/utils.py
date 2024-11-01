import os
from fastapi import UploadFile
from pathlib import Path

UPLOAD_FOLDER = Path("uploads")

def save_upload_file(upload_file: UploadFile, destination: Path) -> Path:
    file_path = UPLOAD_FOLDER / upload_file.filename
    with file_path.open("wb") as buffer:
        buffer.write(upload_file.file.read())
    return file_path

def remove_file(file_path: Path):
    try:
        os.remove(file_path)
    except Exception as e:
        print(f"Error deleting file: {e}")

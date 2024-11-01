from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.model import predict_ecg
from app.utils import save_upload_file, remove_file

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def upload_page(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@app.post("/upload", response_class=HTMLResponse)
async def handle_file_upload(request: Request, file: UploadFile = File(...)):
    if not file.filename.endswith(".h5"):
        return templates.TemplateResponse("upload.html", {
            "request": request,
            "error": "Invalid file format. Please upload an HD5 file."
        })

    file_path = save_upload_file(file, Path("uploads"))
    predictions = predict_ecg(file_path)
    remove_file(file_path)

    if predictions is None:
        return templates.TemplateResponse("upload.html", {
            "request": request,
            "error": "Error processing file. Please try again."
        })

    return templates.TemplateResponse("results.html", {
        "request": request,
        "predictions": predictions
    })

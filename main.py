from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from model import predict
from PIL import Image
import io
import platform

import pathlib
plt = platform.system()
if plt == 'Windows': pathlib.PosixPath = pathlib.WindowsPath
if plt == 'Linux': pathlib.WindowsPath = pathlib.PosixPath

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to MohammedAPI!"}

@app.post("/predict")
async def predict_image(image: UploadFile):
    contents = image.file.read() 
    img = Image.open(io.BytesIO(contents))

    if img.mode != "RGB":
        img = img.convert("RGB")
    
    if img is None:
        return {"error": "Invalid image"}

    pred, prob, description = predict(img)
    return {"prediction": pred, "probability": prob, "description": description}
from fastapi import FastAPI
import os
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/")

def root():
    return("Homepage is working!")

@app.get("/demo")

def predict_dummy():
    return {
        "video": "demo_dashcam.mp4",
        "detections": [
            {"label": "stop", "confidence": 0.94, "bbox": [100, 200, 150, 250]},
            {"label": "green_light", "confidence": 0.91, "bbox": [300, 100, 340, 140]}
        ]
    }

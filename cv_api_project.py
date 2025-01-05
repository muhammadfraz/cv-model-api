"""
CV Model API Service

A REST API to serve pre-trained computer vision models for tasks like image 
classification and object detection. This script integrates model loading, 
prediction endpoints, and basic server setup.

Usage:
1. Install dependencies: pip install fastapi uvicorn torch torchvision pillow
2. Run the server: uvicorn cv_api_project:app --reload
"""

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from typing import List
from PIL import Image
import torch
from torchvision import models, transforms
import io

# Initialize FastAPI application
app = FastAPI(title="CV Model API Service", description="Serve ML Models via REST API")

# Load pre-trained model
MODEL = models.resnet50(pretrained=True)
MODEL.eval()

# Define image preprocessing transforms
TRANSFORM = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Load class labels (for classification)
with open("data/imagenet_classes.txt", "r") as f:
    CLASS_LABELS = [line.strip() for line in f.readlines()]

# Helper function: Image preprocessing
def preprocess_image(image: Image.Image) -> torch.Tensor:
    return TRANSFORM(image).unsqueeze(0)

# API Endpoints
@app.get("/health/")
def health_check():
    """Check API health status."""
    return {"status": "healthy"}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    """Make a prediction using the pre-trained model."""
    try:
        # Read image file
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        tensor = preprocess_image(image)

        # Perform inference
        with torch.no_grad():
            outputs = MODEL(tensor)
            probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
            top5_prob, top5_catid = torch.topk(probabilities, 5)

        # Prepare response
        predictions = [
            {"label": CLASS_LABELS[catid], "probability": prob.item()}
            for prob, catid in zip(top5_prob, top5_catid)
        ]
        return {"predictions": predictions}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("cv_api_project:app", host="0.0.0.0", port=8000, reload=True)

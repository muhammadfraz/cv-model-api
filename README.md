# CV Model API Service

This repository provides a **REST API** for serving pre-trained computer vision models. It enables users to perform **image classification** or **object detection** using state-of-the-art models through a simple and scalable API. The project is built with **FastAPI** and designed for easy deployment, extensibility, and efficient usage of machine learning models.

---

## **Features**
- Serve pre-trained models for **image classification** and **object detection**.
- Supports both **real-world** and **simulated datasets**.
- Extensible for additional computer vision tasks.
- Easy-to-deploy architecture using **Docker** and **cloud-ready tools**.
- Built-in **logging** and **error handling** for robust performance.

---

## **Tech Stack**
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Machine Learning**: [PyTorch](https://pytorch.org/), [TorchVision](https://pytorch.org/vision/stable/index.html)
- **Tools**: Docker, Fiftyone (optional)
- **Deployment**: Supports Kubernetes, GCP, or local environments.

---

## **Getting Started**

### Prerequisites
- Python 3.8+
- Pip package manager
- Docker (optional, for deployment)

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/cv-api-project.git
   cd cv-api-project

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Download the pre-trained model: Run the provided script to download a ResNet-50 model:**
   ```bash
   python scripts/download_model.py

4. **Run the API:**
   ```bash
   uvicorn app.main:app --reload

## **Testing the API**
Use Postman, cURL, or any HTTP client to test the endpoints.

Example (cURL):
   ```bash
   curl -X POST "http://127.0.0.1:8000/predict/" -F "file=@data/example_images/sample.jpg"
   ```

## **Endpoints**

1. /predict/
- Method: POST
- Description: Accepts an image file and returns a prediction.
- Request:
   - Content-Type: multipart/form-data
   - File: An image file (e.g., .jpg, .png)
- Response:
   ```json
   {
      "prediction": "golden retriever"
   }
   ```

2. /health/
- Method: GET
- Description: Returns the health status of the API.
- Response:
   ```json
   {
      "status": "healthy"
   }

## Things To Do
1. Test with model
2. Write tests

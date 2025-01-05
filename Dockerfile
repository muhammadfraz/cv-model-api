# Use official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "cv_api_project:app", "--host", "0.0.0.0", "--port", "8000"]

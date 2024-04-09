# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY backend/requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --progress-bar off --privileged --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY backend/ .

# Expose the port that FastAPI will run on
EXPOSE 8000

# Define the command to run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

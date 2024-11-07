#!/bin/bash

echo "Setting up ECG2AF Web Application..."

# Step 1: Check if Docker is installed
if ! command -v docker &> /dev/null
then
    echo "Docker is not installed. Installing Docker..."
    # Provide a message to guide the user to install Docker manually
    echo "Please download and install Docker from https://www.docker.com/products/docker-desktop"
    exit 1
else
    echo "Docker is already installed."
fi

# Step 2: Check if Git LFS is installed
if ! git lfs &> /dev/null
then
    echo "Git LFS is not installed. Installing Git LFS..."
    if command -v brew &> /dev/null
    then
        brew install git-lfs
    else
        echo "Please install Git LFS manually from https://git-lfs.github.com/"
        exit 1
    fi
    git lfs install
else
    echo "Git LFS is already installed."
fi

# Step 3: Pull the Docker image for required libraries
echo "Pulling Docker image..."
docker pull ghcr.io/broadinstitute/ml4h:tf2.9-latest-cpu

# Step 4: Clone the repository if not already done
if [ ! -d "ml4h" ]; then
    echo "Cloning the repository..."
    git clone https://github.com/broadinstitute/ml4h.git
    cd ml4h
else
    echo "Repository already exists, navigating to it..."
    cd ml4h
fi

# Step 5: Install Git LFS and pull the model
echo "Installing Git LFS and pulling the model..."
git lfs install
if [ ! -f "model_zoo/ECG2AF/ecg_5000_survival_curve_af_quadruple_task_mgh_v2021_05_21.h5" ]; then
    git lfs pull --include model_zoo/ECG2AF/ecg_5000_survival_curve_af_quadruple_task_mgh_v2021_05_21.h5
    git lfs pull --include model_zoo/ECG2AF/strip_*
else
    echo "Model already exists. Skipping model pull."
fi

# Navigate back to the main directory before building the Docker container
cd ..

# Step 6: Build Docker image
echo "Building Docker image..."
docker build -t ecg2af-web-app .

# Step 7: Run the Docker container
echo "Running the Docker container on port 8000 ..."
docker run -d -p 8000:8000 --name ecg2af-web-app-container ecg2af-web-app

# Completion message with usage information
echo "ECG2AF Web Application is running on http://localhost:8000"
echo "API documentation available at http://localhost:8000/docs"
echo "To stop: docker stop ecg2af-web-app-container"
echo "To remove: docker rm ecg2af-web-app-container (after stopping)"
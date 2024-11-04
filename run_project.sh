#!/bin/bash

# Step 1: Pull the Docker image for required libraries
echo "Pulling Docker image..."
docker pull ghcr.io/broadinstitute/ml4h:tf2.9-latest-cpu

# Step 2: Clone the repository if not already done
if [ ! -d "ml4h" ]; then
    echo "Cloning the repository..."
    git clone https://github.com/broadinstitute/ml4h.git
    cd ml4h
else
    echo "Repository already exists, navigating to it..."
    cd ml4h
fi

# Step 3: Install Git LFS and pull the model
echo "Installing Git LFS and pulling the model..."
git lfs install
if [ ! -f "model_zoo/ECG2AF/ecg_5000_survival_curve_af_quadruple_task_mgh_v2021_05_21.h5" ]; then
    git lfs pull --include model_zoo/ECG2AF/ecg_5000_survival_curve_af_quadruple_task_mgh_v2021_05_21.h5
else
    echo "Model already exists. Skipping model pull."
fi

# Step 4: Build the Docker container
# Adjust the Dockerfile path to account for the Source directory structure
echo "Building the Docker container..."
docker build -t ecg2af-web-app .

# Step 5: Run the Docker container
echo "Running the Docker container..."
docker run -p 8000:8000 --name ecg2af-web-app-container ecg2af-web-app
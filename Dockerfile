# Use the official ml4h container from Broad Institute as the base image
FROM ghcr.io/broadinstitute/ml4h:tf2.9-latest-cpu

# Set the working directory in the container
WORKDIR /ECG2AF_WebApp

# Copy the requirements file into the container
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Source directory into the container
COPY Source /ECG2AF_WebApp/Source

# Copy the Templates directory into the container
COPY Templates /ECG2AF_WebApp/Templates

# Copy the ml4h directory into the container, including the model file
COPY ml4h /ECG2AF_WebApp/ml4h

# Set the working directory to the Source directory
WORKDIR /ECG2AF_WebApp/Source

# Command to run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

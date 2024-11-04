# Use an official Python runtime as a parent image
FROM python:3.8

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

# Set the working directory to the Source directory
WORKDIR /ECG2AF_WebApp/Source

# Command to run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
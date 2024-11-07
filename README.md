# 🌟 ECG2AF Web Application

Welcome to the ECG2AF Web Application! This application allows users to predict the risk of atrial fibrillation (AF) using ECG data uploaded in HD5 format. The application is built with FastAPI and uses a pre-trained model to process uploaded ECG files and return multi-task predictions.

---

## 📋 Table of Contents
- [🖥️ Overview](#overview)
- [🚀 Features](#features)
- [🔧 Setup Instructions](#setup-instructions)
- [📂 Project Structure](#project-structure)
- [📂 Detailed File Descriptions](#Detailed-File-Descriptions)
- [🐳 Dockerfile](#Dockerfile)
- [⚙️ Usage](#usage)
- [🌐 Scalability](#scalability)
- [💡 Assumptions](#assumptions)
- [🛡️ Error Handling](#error-handling)
- [📜 License](#license)

---

## 🖥️ Overview
This web application leverages FastAPI to process ECG files stored in `.hd5` format and runs predictions using a pre-trained **ECG2AF** model. Designed for simplicity, it offers a smooth user experience and can be deployed locally with minimal effort.

> **Why ECG2AF?**  
> Atrial fibrillation (AF) is a major risk factor for stroke and heart failure. Predicting AF using data-driven methods can greatly assist clinicians in early diagnosis and treatment planning.

---

## 🚀 Features

✨ **File Upload Interface**  
A simple, user-friendly upload portal that allows users to submit their ECG files for analysis.

⚡ **Real-Time Processing**  
Get results instantly, thanks to the efficient processing of ECG data and multi-task prediction outputs.

🛡️ **Robust Error Handling**  
Receive clear, actionable feedback for any issues encountered (e.g., incorrect file formats).

😊 **User Friendly** 
Provides API documentation and a web interface for easy testing. Includes both pre-trained and test models for verification and testing.

> **Unique Approach**: This tool is tailored for quick integration with clinical workflows and can be adapted for other prediction models.

---

## 🛠️ Setup and Installation

Follow these steps to get the application running on your local environment:

Prerequisites
```   
      * Python 3.6 or higher
      * Docker
      * Git LFS (for large file storage to download the model)
```

### 1. Clone the Repository
Clone the project from GitHub and navigate into the project folder:
```bash
git clone https://github.com/MOJTABAFA/ECG2AF_WebApp.git
cd ECG2AF_WebApp
```

### 2. Pull the Docker Image
To ensure all necessary libraries are available, pull the pre-configured Docker image:
```bash
docker pull ghcr.io/broadinstitute/ml4h:tf2.9-latest-cpu
```

### 3. Install Git LFS and Download the Model
Git LFS (Large File Storage) is needed to pull the model file:
```bash
git lfs install
git lfs pull --include model_zoo/ECG2AF/ecg_5000_survival_curve_af_quadruple_task_mgh_v2021_05_21.h5
git lfs pull --include model_zoo/ECG2AF/strip_*
```

### 4. Install Dependencies
Ensure Python 3.6 or higher is installed. Run the following command to install the required packages:
```bash
pip install -r requirements.txt
```

### 5. Run the Application
Start the application locally using Uvicorn:
```bash
uvicorn main:app --reload
```
---

### 6. Automated Run with Bash Script
Use the provided setup.sh script to automate setup, including Docker build and deployment

```bash
bash setup.sh
```

> **Tip**: Ensure your Python environment is activated before running the commands.

---

## 📂 Project Structure
Here's a brief overview of the project structure to help you navigate the files:
```plaintext
📁 ECG2AF_WebApp
├── Source
│   ├── main.py         # Core FastAPI application
│   ├── model.py        # Model loading and prediction functions
│   └── utils.py        # Utility functions for ECG data processing
├── Models              # Folder containing pre-trained and test models
│   ├── ecg_5000_survival_curve_af_quadruple_task_mgh_v2021_05_21.h5
│   └── fake_0.hd5      # Test model file for initial testing
├── Templates
│   ├── upload.html     # File upload interface
│   └── results.html    # Displays prediction results
├── Dockerfile          # Docker configuration for deployment
├── README.md           # Project documentation
├── requirements.txt    # List of required packages
├── ECG2AF_API_Guide.pdf# Instructions for Setting Up and Using the ECG2AF Web Application API
└── setup.sh            # Bash script for automated setup and deployment

```

> **Note**: The `Source` folder contains all Python scripts, organized for logical separation and improved maintainability. Additionally, models are saved in the `Models` folder to ensure accessibility in case of any issues retrieving them from the `Broad Institute's` GitHub repository.

## 📂 Detailed File Descriptions

### 1. `Source/main.py`
The core application script that sets up the FastAPI server, handles file uploads, processes ECG data, and renders prediction results.

### 2. `Source/model.py`
Handles loading the pre-trained ECG2AF model and making predictions on the input ECG data.

### 3. `Source/utils.py`
Contains utility functions for processing and normalizing ECG data from uploaded `.hd5` files.

### 4. `Templates/upload.html`
Provides a simple interface for users to upload their ECG files.

### 5. `Templates/results.html`
Displays the prediction results in a structured format.

## 📦 Requirements
List of dependencies included in `requirements.txt`:
```plaintext
fastapi== 0.78.0
uvicorn== 0.17.6
h5py== 3.7.0
numpy== 1.21.6
tensorflow== 2.9.0
tensorflow-addons== 0.17.1
jinja2== 3.1.2
python-multipart== 0.0.5

```

## 🐳 Dockerfile
The `Dockerfile` sets up the environment for running the application in a containerized format.
```dockerfile
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

```
> **Note**: Place the model in the specified path for accurate predictions.



---
## ⚙️ Run with Docker

1. Build the Docker Image  
   `docker build -t ecg2af-web-app . `

2. Run the Docker Container
   `docker run -d -p 8000:8000 --name ecg2af-web-app-container ecg2af-web-app`

---

## ⚙️ Usage

1. Access the API documentation at `http://localhost:8000/docs` in your browser for interactive testing.  
   This will open the interactive API documentation provided by FastAPI.

2. Use the `/upload/` endpoint to upload your `.hd5` ECG file and receive multi-task predictions.

> **Pro Tip**: Use the API documentation to test the upload functionality and verify responses before integrating with other systems.

---

## 🌐 Scalability
Scaling the ECG2AF application for higher user loads and larger datasets can be achieved through a comprehensive, multi-faceted strategy. Implementing technologies such as Kubernetes for orchestrating containerized services provides robust and reliable scaling. For processing large volumes of data, integrating distributed data frameworks like Apache Spark or Dask enhances batch processing efficiency. (I really love Dask which is an excellent choice due to its seamless compatibility with Python and straightforward deployment on cloud platforms like AWS, GCP, and Azure!). Additionally, leveraging serverless architectures with services like AWS Lambda or Azure Functions supports on-demand scaling, optimizing resource allocation and reducing costs.

- **Batch Processing**: Implement batch processing using distributed frameworks such as Apache Spark or Dask to analyze large volumes of ECG data concurrently, thereby boosting processing efficiency. Integrating a task queue system like **Celery** with **Redis** can further enhance the asynchronous handling of multiple file uploads.

- **Load Balancing**: Deploy on cloud platforms (e.g., **AWS**, **GCP**) with load balancing and auto-scaling to handle traffic spikes.

- **Distributed Processing**: Utilize Apache Spark for parallel data processing to handle extensive datasets effectively. This ensures that large-scale data analysis remains efficient and responsive.

- **Cloud Hosting**: Host the application on cloud services such as **AWS** or **GCP** to harness scalable infrastructure. Employ cloud storage solutions like **AWS S3** to manage and store uploaded files, accommodating growing storage demands.

- **Serverless Architecture**: For individual file processing, serverless functions (e.g., **AWS Lambda**) offer a scalable, on-demand solution that adapts to fluctuating file upload frequencies without constant server management.

> **Scalability Insight**: Combining these strategies ensures a scalable, resilient, and high-performing application capable of handling substantial data loads and user demands seamlessly.

---

## 💡 Assumptions
- The pre-trained model file is correctly placed in the specified path.
- All uploaded files conform to the `.hd5` format for seamless processing.

> **Clarification**: This application is designed for standard `.hd5` files used in clinical ECG data storage. Ensure data is properly pre-processed if adapting for different input types.

---
## ✨ Model Output Details ( Not entirely accurate—these are just my estimates based on the predicted results and the surrounding context.)

```Plaintext
   Prediction 1: Confidence scores for different intervals.
   Prediction 2: Binary classification probabilities.
   Prediction 3: Scalar risk metric.
   Prediction 4: Binary classification output.
```
---

## 🛡️ Error Handling
We’ve designed the application with user experience in mind:
- **Invalid File Format**: If a non-`.hd5` file is uploaded, a helpful error message is shown.
- **Processing Errors**: Any unexpected issues during file reading or data conversion trigger detailed HTTP responses with specific guidance.

> **Error Handling Strategy**: Clear error messages help users quickly identify issues and take corrective actions, ensuring smooth operation.

---
## 📜 License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## 📧 Contact

💡 For any questions or suggestions, please feel free to contact me at mfazli@stanford.edu

💡 © Mojtaba Fazli Nov, 2024.



# 🌟 ECG2AF Web Application

Welcome to the **ECG2AF Web Application**! This project is a FastAPI-based web tool designed to make uploading and processing ECG files seamless while predicting the risk of atrial fibrillation with precision. Dive into the details below to see how you can get started quickly.

---

## 📋 Table of Contents
- [Overview](#overview)
- [🚀 Features](#features)
- [🔧 Setup Instructions](#setup-instructions)
- [📂 Project Structure](#project-structure)
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

> **Unique Approach**: This tool is tailored for quick integration with clinical workflows and can be adapted for other prediction models.

---

## 🔧 Setup Instructions

Follow these steps to get the application running on your local environment:

### 1. Clone the Repository
Clone the project from GitHub and navigate into the project folder:
```bash
git clone https://github.com/broadinstitute/ml4h.git
cd ml4h
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


### 6. Automated Run with Bash Script
Run the entire setup with:
```bash
./run_project.sh
```

> **Tip**: Ensure your Python environment is activated before running the commands.

---

## 📂 Project Structure
Here's a brief overview of the project structure to help you navigate the files:
```plaintext
📁 ECG2AF Web Application
├── Source
│   ├── main.py         # Core FastAPI application
│   ├── model.py        # Model loading and prediction functions
│   └── utils.py        # Utility functions for ECG data processing
├── Templates
│   ├── upload.html     # Provides a simple interface for users to upload their ECG files.
│   └── results.html    # Displays the prediction results in a structured format.
├── Dockerfile          # Docker configuration for deployment
├── README.md           # Project Readme file
├── requirements.txt    # List of required packages
└── run_project.sh      # Bash file for automated run
```

> **Note**: The `Source` folder contains all Python scripts for logical separation and better maintainability.

---

## ⚙️ Usage

1. Visit `http://localhost:8000/docs` in your web browser.  
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

## 🛡️ Error Handling
We’ve designed the application with user experience in mind:
- **Invalid File Format**: If a non-`.hd5` file is uploaded, a helpful error message is shown.
- **Processing Errors**: Any unexpected issues during file reading or data conversion trigger detailed HTTP responses with specific guidance.

> **Error Handling Strategy**: Clear error messages help users quickly identify issues and take corrective actions, ensuring smooth operation.

---

## 📜 License
This project is distributed under the [MIT License](LICENSE), allowing you to use, modify, and distribute the application freely.

> **Open Source Commitment**: Contribute, adapt, or extend this project under the flexibility of the MIT license.

---

🔗 **Want to contribute or learn more? Visit [GitHub page](https://github.com/broadinstitute/ml4h).**

🌟 Thank you for exploring the ECG2AF Web Application. Your feedback and contributions are welcome!

---


💡 For any questions or suggestions, please feel free to contact me either at  mfazli@meei.harvard.edu or mfazli@stanford.edu

💡 © Mojtaba Fazli Nov, 2024. 

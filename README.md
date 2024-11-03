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
├── requirements.txt    # Project dependencies
└── Dockerfile          # Docker configuration for deployment
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
To scale this application for greater user loads and larger data sets, consider the following approaches:

- **Batch Processing**: Integrate a task queue system like **Celery** with **Redis** for processing multiple file uploads asynchronously.
- **Load Balancing**: Deploy on cloud platforms (e.g., **AWS**, **GCP**) with load balancing and auto-scaling to handle traffic spikes.
- **Distributed Processing**: Utilize **Apache Spark** for parallel data processing, enabling efficient handling of massive data sets.

> **Scalability Insight**: Combining these strategies ensures seamless scaling, optimal performance, and resilience under high data loads.

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

🔗 **Want to contribute or learn more? Visit [our GitHub page](https://github.com/broadinstitute/ml4h).**

🌟 Thank you for exploring the ECG2AF Web Application. Your feedback and contributions are welcome!

---

💡 *Crafted with precision and care by clinical AI experts.*


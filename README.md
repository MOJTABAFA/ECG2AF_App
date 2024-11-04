### README.md for ECG2AF Web Application

# ECG2AF Web Application

Welcome to the **ECG2AF Web Application**! This project is designed to help predict the risk of atrial fibrillation (AF) from uploaded ECG data using a pre-trained deep learning model. The application is built using **FastAPI** and supports file uploads for processing ECG data stored in HD5 format.

## 📁 Project Structure
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

## 🚀 Features
- Upload an ECG file in `.hd5` format.
- Process the uploaded ECG data using the pre-trained **ECG2AF model**.
- Display prediction results in a user-friendly format.

## 🛠️ Setup and Installation

### Prerequisites
- Python 3.6 or higher
- Docker (optional for containerized deployment)

### Installation Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/ECG2AF_WebApp.git
   cd ECG2AF_WebApp
   ```
2. **Pull the Docker Image**
   To ensure all necessary libraries are available, pull the pre-configured Docker image:
   ```bash
   docker pull ghcr.io/broadinstitute/ml4h:tf2.9-latest-cpu
   ```
3. Install Git LFS and Download the Model
   Git LFS (Large File Storage) is needed to pull the model file:
   ```bash
   git lfs install
   git lfs pull --include model_zoo/ECG2AF/ecg_5000_survival_curve_af_quadruple_task_mgh_v2021_05_21.h5
   ```

4. **Install Dependencies**
   Install required Python packages by running:
   ```bash
   pip install -r requirements.txt
   ```
5. **Run the Application**
   Navigate to the `Source` directory and start the FastAPI server:
   ```bash
   cd Source
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

### Run with Docker
1. **Build the Docker Image**
   ```bash
   docker build -t ecg2af-web-app .
   ```
2. **Run the Docker Container**
   ```bash
   docker run -p 8000:8000 ecg2af-web-app
   ```

### Run Project with Bash Script
You can automate the setup and run process with the provided `run_project.sh` script:
```bash
bash run_project.sh
```

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
fastapi
uvicorn
h5py
numpy
tensorflow
jinja2
```

## 🐳 Dockerfile
The `Dockerfile` sets up the environment for running the application in a containerized format.
```dockerfile
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
This project is licensed under the MIT License. See the `LICENSE` file for details.

## 📧 Contact

💡 For any questions or suggestions, please feel free to contact me either at mfazli@meei.harvard.edu or mfazli@stanford.edu

💡 © Mojtaba Fazli Nov, 2024.



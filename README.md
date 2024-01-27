# Info Harvest 

## 1. Overview
---
- Summarizing research papers: LLMs can be used to generate summaries of research papers, which can help students and working professionals quickly understand the main points of a paper without having to read the entire document.
- Translating research papers: LLMs can be used to translate research papers from one language to another, which can help students and working professionals access research that is not available in their native language.
- Answering questions about research papers: LLMs can be used to answer questions about research papers, which can help students and working professionals understand the material better and to identify areas where they need more information.

## 2. Motivation
---
LLMs have the potential to make research papers more accessible and easier to use for students and working professionals. This can lead to increased engagement, comprehension, and retention of information.


## 4. Requirements & Constraints
---
### 4.1 Functional Requirements

The web application should provide the following functionality:

- Gemini API Key which is free to use

### 4.2 Non-functional Requirements

The web application should meet the following non-functional requirements:

- The web application should be responsive and easy to use.
- The web application should be secure and protect user data.

### 4.3 Constraints

- The application should be built using Flask and deployed using Docker .
- The cost of deployment should be minimal.

### 4.4 Out-of-scope

- Integrating with external applications or data sources.
- Providing detailed equipment diagnostic information.

## 5. Methodology
---
### 5.1. Problem Statement

Students and working professionals often spend a significant amount of time reading research papers. This can be a time-consuming and challenging task, especially for those who are not familiar with the specific research area.

### 5.2. Data

It takes the Pdf/Docx as a Input and it convert into text data 

### 5.3. Techniques
We will use pretrained object-detection model for data scraping, and a Large language model for genarate insights for data. The following machine learning techniques will be used:

- Scrap Pdf/Docx using CV techniques
- Data preprocessing and cleaning
- Create a prompt dynamicaly
- Using Gemini API retrive the info which required
- Again Preprocess the output data 
- Display the data clearly

## 6. Architecture
---
The web application architecture will consist of the following components:

- A frontend web application built using Html,CSS
- A backend server built using Flask
- A Gemini API (Large Language model) for getting outputs
- Docker containers to run the frontend, backend, and model
- Cloud infrastructure to host the application
- CI/CD pipeline using GitHub Actions for automated deployment

The frontend will interact with the backend server through API calls to request predictions, model training, and data storage. The backend server will manage user authentication, data storage, and model training. The machine learning model will be trained and deployed using Docker containers. The application will be hosted on Digital Ocean droplets. The CI/CD pipeline will be used to automate the deployment process.

## 7. Pipeline
---
The MLOps (Machine Learning Operations) pipeline project is designed to create an end-to-end workflow for developing and deploying a web application that performs data preprocessing, model training, model evaluation, and prediction. The pipeline leverages Docker containers for encapsulating code, artifacts, and both the frontend and backend components of the application. The application is deployed on a DigitalOcean droplet to provide a cloud hosting solution.

The pipeline follows the following sequence of steps:

`Data`: The pipeline starts with the input data, which is sourced from a specified location. It can be in the form of a CSV file or any other supported format.

`Preprocessing`: The data undergoes preprocessing steps to clean, transform, and prepare it for model training. This stage handles tasks such as missing value imputation, feature scaling, and categorical variable encoding.

`Model Training`: The preprocessed data is used to train machine learning models. The pipeline supports building multiple models, allowing for experimentation and comparison of different algorithms or hyperparameters.

`Model Evaluation`: The trained models are evaluated using appropriate evaluation metrics to assess their performance. This stage helps in selecting the best-performing model for deployment.

`Docker Container`: The pipeline utilizes Docker containers to package the application code, model artifacts, and both the frontend and backend components. This containerization ensures consistent deployment across different environments and simplifies the deployment process.

`DigitalOcean Droplet`: The Docker container, along with the required dependencies, is deployed on a DigitalOcean droplet. DigitalOcean provides a cloud hosting solution that allows for scalability, reliability, and easy management of the web application.

`Web App`: The web application is accessible via a web browser, providing a user-friendly interface for interacting with the prediction functionality. Users can input new data and obtain predictions from the deployed model.

`Prediction`: The deployed model uses the input data from the web application to generate predictions. These predictions are then displayed to the user via the web interface.

`Data`: The predicted data is captured and stored, providing a record of the predictions made by the web application. This data can be used for analysis, monitoring, or further processing as needed.

`CI/CD Pipeline`: The pipeline is automated using GitHub Actions, which allows for continuous integration and deployment of the application. This automation ensures that the application is always up-to-date and provides a consistent experience for users.


## 8. Conclusion

Large language models (LLMs) have the potential to revolutionize the way that students and working professionals access and use research information. LLMs can be used to develop tools and applications that can help students and working professionals read and understand research papers more efficiently and effectively. This can lead to reduced time spent reading research papers, improved comprehension and retention of information, increased engagement with research material, and more efficient and effective use of research information.

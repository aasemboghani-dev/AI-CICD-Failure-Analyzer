# AI-Powered CI/CD Failure Analysis & Root Cause Assistant

An AI-powered DevOps/SRE solution that automatically analyzes CI/CD pipeline failures and generates root cause analysis, error classification, suggested fixes, and confidence using an LLM.

## 🚀 Overview

In traditional CI/CD pipelines, engineers often need to manually inspect Jenkins logs to identify why a build or test failed.

This project automates failure analysis by connecting Jenkins with AWS Lambda and the OpenAI Responses API.

When a CI/CD pipeline fails, the system:

1. Captures available failure logs
2. Sends the logs to AWS Lambda
3. Processes the failure information
4. Sends the logs to an LLM
5. Generates an AI-powered root cause analysis
6. Provides a suggested remediation

## 🏗️ Architecture

```text
Developer
    |
    | git push
    v
GitHub
    |
    | Webhook
    v
Jenkins CI/CD
    |
    +--> Install Dependencies
    |
    +--> Run Tests
    |
    +--> Docker Build
    |
    v
Pipeline Failure
    |
    v
Failure Log Capture
    |
    v
AWS Lambda
    |
    v
OpenAI Responses API
    |
    v
AI Root Cause Analysis
    |
    +--> Error Type
    +--> Root Cause
    +--> Suggested Fix
    +--> Confidence
```

## 🛠️ Technologies

### Cloud

- AWS Lambda
- AWS IAM
- AWS Lambda Function URL

### DevOps & CI/CD

- Jenkins
- GitHub
- GitHub Webhooks
- Docker
- Git

### GenAI

- OpenAI API
- OpenAI Responses API
- GPT-5.6 Luna

### Programming & Testing

- Python
- Groovy
- Flask
- Pytest

## 📁 Project Structure

```text
AI-CICD-Failure-Analyzer/
│
├── app/
│   ├── __init__.py
│   └── app.py
│
├── tests/
│   └── test_app.py
│
├── lambda/
│   ├── lambda_function.py
│   ├── requirements.txt
│   └── lambda_function.zip
│
├── Jenkinsfile
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ CI/CD Pipeline

The Jenkins pipeline contains the following stages:

### 1. Checkout

Jenkins retrieves the latest source code from the GitHub repository.

### 2. Install Dependencies

Python dependencies are installed from `requirements.txt`.

### 3. Run Tests

Pytest executes the application test suite.

Test output is captured for failure analysis.

### 4. Docker Build

The application is containerized using Docker.

Docker build output is captured separately for Docker-related failures.

### 5. Failure Analysis

When a pipeline failure occurs, Jenkins collects the available logs and sends them to the AWS Lambda Function URL.

### 6. AI Analysis

AWS Lambda sends the failure information to the OpenAI Responses API.

The AI analyzes the CI/CD failure and returns a structured response.

## 🤖 AI Output

The analysis format is:

```text
Error Type:
Root Cause:
Suggested Fix:
Confidence:
```

Example:

```text
Error Type: ImportError during pytest test collection

Root Cause:
The application imported an invalid class from the Flask package,
preventing the test module from loading.

Suggested Fix:
Use the correct Flask class and rerun the CI pipeline.

Confidence:
100%
```

## 🧪 Failure Scenarios Tested

### Scenario 1 — Test Assertion Failure

An incorrect test assertion was intentionally introduced.

```text
Jenkins Test Stage    → FAILURE
Lambda                → SUCCESS
OpenAI Analysis       → SUCCESS
Root Cause Analysis   → Generated
```

### Scenario 2 — Python Import Failure

The Flask import was intentionally modified to create an import error.

```text
Pytest Collection     → FAILURE
Lambda                → SUCCESS
OpenAI Analysis       → SUCCESS
Root Cause Analysis   → Generated
```

### Scenario 3 — Docker Build Failure

The Docker base image was intentionally changed to an invalid image:

```dockerfile
FROM python:999.99-slim
```

Docker correctly detected the invalid image and failed the build.

```text
Run Tests             → SUCCESS
Docker Build          → FAILURE
Lambda                → SUCCESS
OpenAI API            → SUCCESS
```

The Dockerfile was subsequently restored and the Jenkins pipeline returned to a successful green build.

## 🔐 Security

- OpenAI API credentials are stored as AWS Lambda environment variables.
- Secrets are not hardcoded in the application source code.
- API keys and credentials should never be committed to GitHub.
- AWS IAM is used for controlled access to AWS resources.

## 🎯 Key Features

- Automated CI/CD failure detection
- Jenkins pipeline integration
- Failure log collection
- AWS Lambda serverless processing
- LLM-powered root cause analysis
- Error classification
- Suggested remediation
- Confidence scoring
- Docker build failure analysis support

## 📈 DevOps / SRE Benefits

The solution helps engineers:

- Reduce manual
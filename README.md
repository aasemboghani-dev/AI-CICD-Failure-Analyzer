# AI CI/CD Failure Analyzer

An automated DevOps project that detects CI/CD pipeline failures, captures test logs, and analyzes the failure using AWS Lambda to provide a root cause and recommended fix.

## Architecture

GitHub
   ?
Jenkins Webhook
   ?
Jenkins CI/CD Pipeline
   ?
Pytest
   ?
Docker Build
   ?
Failure Detection
   ?
AWS Lambda
   ?
Root Cause Analysis
   ?
Recommended Fix

## Technologies Used

- Python
- Flask
- Pytest
- Git & GitHub
- Jenkins
- Docker
- AWS Lambda
- AWS IAM
- AWS Lambda Function URL
- PowerShell

## Project Workflow

1. Developer pushes code to GitHub.
2. GitHub Webhook triggers the Jenkins pipeline.
3. Jenkins checks out the source code.
4. Jenkins installs Python dependencies.
5. Pytest automatically runs application tests.
6. If tests fail, Jenkins captures the test output.
7. Jenkins sends the failure log to AWS Lambda.
8. AWS Lambda analyzes the failure.
9. Lambda returns:
   - Root cause
   - Recommended fix
   - Original failure log
10. If tests pass, Jenkins continues to the Docker build stage.

## Failure Analysis Example

Example CI failure:

    FAILED tests/test_app.py - assert 200 == 500

Lambda analysis:

    Root Cause:
    The pytest expected HTTP 500, but the Flask application returned HTTP 200.

    Recommended Fix:
    Change the test assertion from status_code == 500 back to status_code == 200.

## Jenkins Pipeline

The Jenkins pipeline contains the following stages:

- Checkout
- Install Dependencies
- Run Tests
- Docker Build

Failure handling is implemented using Jenkins post-build actions. When the pipeline fails, the captured test output is sent to the AWS Lambda Function URL.

## Docker

The application is containerized using Docker.

Build the image:

    docker build -t ai-cicd-failure-analyzer .

Run the container:

    docker run -d -p 5000:5000 --name ai-cicd-analyzer ai-cicd-failure-analyzer

Application URL:

    http://localhost:5000

## AWS Lambda

Lambda function:

    AI-CICD-Failure-Analyzer

Runtime:

    Python 3.14

The Lambda function receives a CI/CD failure log and returns a structured analysis containing the root cause and recommended fix.

## Project Structure

    AI-CICD-Failure-Analyzer/
    +-- app/
        +-- __init__.py
        +-- app.py
    +-- tests/
        +-- test_app.py
    +-- lambda_function.py
    +-- Dockerfile
    +-- requirements.txt
    +-- README.md
    +-- .gitignore

## CI/CD Validation

The project was tested with both failure and successful pipeline scenarios.

Failure scenario:

    Pytest failure
        ?
    Jenkins detects failure
        ?
    Failure log captured
        ?
    AWS Lambda invoked
        ?
    Root cause identified
        ?
    Recommended fix returned

Successful scenario:

    GitHub Push
        ?
    Jenkins
        ?
    Pytest PASS
        ?
    Docker Build PASS
        ?
    Jenkins SUCCESS

## Key DevOps Skills Demonstrated

- CI/CD pipeline automation
- Jenkins Pipeline
- GitHub Webhooks
- Automated testing
- Failure handling
- Log collection
- Serverless AWS Lambda
- Docker containerization
- AWS IAM
- Cloud automation
- DevOps troubleshooting

## Future Enhancement

Amazon Bedrock integration can be enabled once model authorization is available for the AWS account. This will allow the rule-based analyzer to be replaced or enhanced with an LLM-based root cause analysis workflow.

## Author

Asim Boghani

GitHub:
https://github.com/aasemboghani-dev

# JobMatchAI

ATS-Friendly Resume & Job Matching Tool

JobMatchAI is a Python and Flask-based portfolio project that compares a resume with a job description and identifies matched and missing technical skills.

## Features

- Resume and job description input
- Automatic skill extraction
- Matched skill detection
- Missing skill detection
- ATS match percentage
- Skill coverage count
- Skill recommendations
- Flask web interface
- Automated tests
- AWS Lambda-ready handler
- Git/GitHub version control

## Technology Stack

- Python
- Flask
- HTML/CSS
- Git & GitHub
- AWS Lambda

## How It Works

Resume
   |
   v
Skill Extraction
   |
   v
Job Description Analysis
   |
   v
Skill Comparison
   |
   +--> Matched Skills
   |
   +--> Missing Skills
   |
   +--> Match Percentage
   |
   +--> Recommendation

## Run Locally

Install dependencies:

pip install -r requirements.txt

Run the application:

python -m app.web

Open:

http://127.0.0.1:5000

## Testing

Run:

python -m pytest -q

Current test result:

3 passed

## AWS Lambda Readiness

The project includes a Lambda-compatible handler in:

lambda_function.py

The handler has been tested locally and successfully returns HTTP 200 with the Flask application response.

A clean Lambda deployment ZIP has also been prepared.

AWS deployment is optional and is kept separate to avoid unnecessary cloud resources and costs.

## Project Structure

JobMatchAI/
|
|-- app/
|   |-- main.py
|   |-- matcher.py
|   |-- parser.py
|   |-- scorer.py
|   |-- web.py
|   `-- __init__.py
|
|-- templates/
|   `-- index.html
|
|-- tests/
|-- lambda_function.py
|-- requirements.txt
`-- README.md

## Project Goal

This project demonstrates practical skills in:

- Python development
- Flask web development
- Text processing
- Rule-based skill matching
- Automated testing
- Git/GitHub
- AWS Lambda deployment concepts

## Author

Sakshi Lokhande
Computer Science & Engineering
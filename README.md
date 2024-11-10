# Pathed - AI-Enhanced Patient Appointment and Diagnosis System

*Pathed* is an AI-powered web application designed to streamline the patient appointment scheduling process and provide a personalized conversation-based diagnostic assistant. This project integrates a patient questionnaire chatbot with a hospital's appointment booking system, providing an efficient way to collect patient information and offer preliminary diagnoses based on conversation history.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Database Setup](#database-setup)
  - [Running the Application](#running-the-application)
- [Demo](#demo)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

Pathed provides patients with a conversational interface to interact with an AI assistant that asks relevant questions, gathers responses, and offers a preliminary diagnostic summary based on input data. The application allows hospital staff to easily schedule, manage, and review patient appointments, incorporating the AI-generated notes from the conversation. Additionally, it stores session information, including conversation history and diagnoses, in a MySQL database for later reference.

## Features

- **AI-Powered Patient Questionnaire**: Conversational chatbot that interacts with patients to gather health information.
- **Preliminary Diagnosis Generation**: Provides initial diagnosis summaries based on patient responses.
- **Appointment Management**: Allows hospital staff to schedule, review, and manage appointments.
- **Session History Storage**: Saves session details such as conversation history and diagnostic information.
- **User Authentication**: Enables secure access for patients and staff using Flask-Login.

## Tech Stack

- **Backend**: Python, Flask, SQLAlchemy
- **Database**: MySQL (deployed on PythonAnywhere)
- **Frontend**: HTML, CSS, JavaScript (Jinja2 for templating)
- **AI Component**: Integrated AI-based dynamic questionnaire for patient responses
- **Deployment**: PythonAnywhere, Vercel (optional for frontend hosting)

## Getting Started

### Prerequisites

- Python 3.10+
- MySQL server (or access to MySQL via PythonAnywhere)
- [Flask](https://flask.palletsprojects.com/), [Flask-Login](https://flask-login.readthedocs.io/), [Flask-Migrate](https://flask-migrate.readthedocs.io/), and other dependencies listed in `requirements.txt`

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/pathed.git
    cd pathed
    ```

2. Set up a virtual environment and install dependencies:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

### Database Setup

1. **Configure MySQL Database**: Update the `config.py` file with your MySQL credentials:

    ```python
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@host/database_name'
    ```

2. **Run Migrations**:

    Initialize the database and run migrations:

    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

### Running the Application

1. Start the Flask application:

    ```bash
    flask run
    ```

2. Access the application in your browser at `http://localhost:5000`.

## Demo

The application demo is hosted at: [https://your-pythonanywhere-username.pythonanywhere.com](https://your-pythonanywhere-username.pythonanywhere.com)  
*Note*: Replace the link with your actual PythonAnywhere app URL.

## Usage

1. **Patient Interaction**:
   - Patients initiate a session and interact with the AI chatbot.
   - The chatbot collects responses, generating a preliminary diagnosis and recording details for future reference.

2. **Appointment Scheduling**:
   - Staff members can view, schedule, or update patient appointments.
   - Each appointment entry stores the patient's session notes, including conversation history and diagnosis.

3. **Accessing the Dashboard**:
   - The user can log in to access the patient or staff dashboard, where they can manage appointments and review chatbot-generated diagnostics.

## Contributing

If you would like to contribute to Pathed:

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.


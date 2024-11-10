Pathed - AI-Enhanced Patient Appointment and Diagnosis System
Pathed is an AI-powered web application designed to streamline the patient appointment scheduling process and provide a personalized conversation-based diagnostic assistant. This project integrates a patient questionnaire chatbot with a hospital's appointment booking system, providing an efficient way to collect patient information and offer preliminary diagnoses based on conversation history.

Table of Contents
Project Overview
Features
Tech Stack
Getting Started
Prerequisites
Installation
Database Setup
Running the Application
Demo
Usage
Contributing
License
Project Overview
Pathed provides patients with a conversational interface to interact with an AI assistant that asks relevant questions, gathers responses, and offers a preliminary diagnostic summary based on input data. The application allows hospital staff to easily schedule, manage, and review patient appointments, incorporating the AI-generated notes from the conversation. Additionally, it stores session information, including conversation history and diagnoses, in a MySQL database for later reference.

Features
AI-Powered Patient Questionnaire: Conversational chatbot that interacts with patients to gather health information.
Preliminary Diagnosis Generation: Provides initial diagnosis summaries based on patient responses.
Appointment Management: Allows hospital staff to schedule, review, and manage appointments.
Session History Storage: Saves session details such as conversation history and diagnostic information.
User Authentication: Enables secure access for patients and staff using Flask-Login.
Tech Stack
Backend: Python, Flask, SQLAlchemy
Database: MySQL (deployed on PythonAnywhere)
Frontend: HTML, CSS, JavaScript (Jinja2 for templating)
AI Component: Integrated AI-based dynamic questionnaire for patient responses
Deployment: PythonAnywhere, Vercel (optional for frontend hosting)
Getting Started
Prerequisites
Python 3.10+
MySQL server (or access to MySQL via PythonAnywhere)
Flask, Flask-Login, Flask-Migrate, and other dependencies listed in requirements.txt
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/pathed.git
cd pathed
Set up a virtual environment and install dependencies:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
Database Setup
Configure MySQL Database: Update the config.py file with your MySQL credentials:

python
Copy code
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@host/database_name'
Run Migrations:

Initialize the database and run migrations:

bash
Copy code
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
Running the Application
Start the Flask application:

bash
Copy code
flask run
Access the application in your browser at http://localhost:5000.

Demo
The application demo is hosted at: https://your-pythonanywhere-username.pythonanywhere.com
Note: Replace the link with your actual PythonAnywhere app URL.

Usage
Patient Interaction:

Patients initiate a session and interact with the AI chatbot.
The chatbot collects responses, generating a preliminary diagnosis and recording details for future reference.
Appointment Scheduling:

Staff members can view, schedule, or update patient appointments.
Each appointment entry stores the patient's session notes, including conversation history and diagnosis.
Accessing the Dashboard:

The user can log in to access the patient or staff dashboard, where they can manage appointments and review chatbot-generated diagnostics.
Contributing
If you would like to contribute to Pathed:

Fork the repository.
Create a new feature branch (git checkout -b feature-branch).
Commit your changes (git commit -m 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a pull request.


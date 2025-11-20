## Overview

📦 PGQueue Demo – Worker + Scheduler Example
This project demonstrates how to use PgQueuer with Python to enqueue jobs and process them asynchronously using a background worker.

## 📥 Installation Instructions

1. Start PostgreSQL
   docker compose up -d

2. Create & activate virtual environment
   cd pgqueue-demo
   python3.12 -m venv venv
   source venv/bin/activate

3. Install dependencies
   pip install -r requirements.txt

4. Install PgQueuer database schema
   pgq --pg-host localhost --pg-port 5555 --pg-user testrunner_queue --pg-password testrunner_queue --pg-database testrunner_queue install

5. Start Worker
   pgq run app.worker:main

6. Schedule a Job
   python app/scheduler.py

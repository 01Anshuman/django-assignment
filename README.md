# Django Internship Assignment

This repository contains the code for my Django internship assignment, completed as part of the tasks assigned. The project implements a Django application with APIs, authentication, and Celery integration.

## Project Overview
- **Task 2: API Development**: Created public and protected API endpoints with Token Authentication and implemented Django login.
- **Task 3: Celery Integration**: Set up Celery with Redis to run a background task for sending welcome emails after user registration.

## Features
- **Public Endpoint**: Accessible at `/api/public/` with a simple message.
- **Protected Endpoint**: Accessible at `/api/protected/` (requires Token Authentication) for CRUD operations on messages.
- **Django Login**: Web-based login at `/login/` using a custom template.
- **User Registration**: API at `/api/register/` to create users and queue a welcome email via Celery.
- **Celery Task**: Sends a welcome email 5 seconds after registration (simulated with console backend).

## Prerequisites
- Python 3.8+
- Django
- djangorestframework
- dj-rest-auth
- django-allauth
- celery
- redis (Windows port)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/01Anshuman/django-assignment.git
   cd django-assignment


2. Creating Virtual envoinment and acitvate it
   ```bash
      python -m venv venv
      venv\Scripts\activate


3. Install dependencies:
   ```bash
      pip install -r requirements.txt


4. Setup envoiment variable:
  - Create a .env file in the root directory with text:

      EMAIL_HOST_USER=your-email@gmail.com
      EMAIL_HOST_PASSWORD=your-app-password


5. Apply migrations:
   ```bash
      python manage.py createsuperuser


6. Creating a superuser:
   ```bash
      python manage.py createsuperuser




## Running the Project

1. Start Redis server:
- Navigate to Redis-x64-3.0.504 (or your Redis folder).
- Run:
   ```bash
      redis-server.exe redis.windows.conf


2. Start Celery worker:
   ```bash
      celery -A myproject worker --loglevel=info

3. Start the Django server:
   ```bash
      python manage.py runserver

4. Access the application at http://127.0.0.1:8000/



## Testing

1. Public Endpoint: 

- Visit http://127.0.0.1:8000/api/public/ (expect {"message": "This is a public endpoint..."}).




2. Protected Endpoint:

- Use Postman with a token (generate via shell) to access http://127.0.0.1:8000/api/protected/.

- Generate token:
   ```bash
      python manage.py shell

   ```python 
      from django.contrib.auth.models import User
      from rest_framework.authtoken.models import Token
      user = User.objects.get(username='admin')
      token, created = Token.objects.get_or_create(user=user)
      print(token.key)

- GET: Expect [] (empty list).

- POST with {"content": "test message"}: Expect a 201 response with new message data.



3. Login: Visit http://127.0.0.1:8000/login/ and log in with superuser credentials.



4. Registration:
- Use Postman to POST to http://127.0.0.1:8000/api/register/ with json: 
   
   ```json
      {
      "username": "test",
      "password": "testpass",
      "email": "test@example.com"
      }

- Expect {"message": "User created successfully, welcome email queued."} (201).

- Check Celery logs for "Welcome email sent to test" after ~5 seconds.

- With console backend, check server terminal for email output.



## Acknowledgements:

1. Guided by Grok 3(xAI)
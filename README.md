# Simple Django Authentication Project

## Description

This is a simple authentication project built with Django. It includes basic user registration, login, password reset functionality, and a protected contact page that is accessible only to logged-in users. The project uses Django's built-in authentication system and demonstrates how to protect views using the `login_required` decorator.

## Features

- User Registration
- User Login
- User Logout
- Password Reset
- Protected Views (Contact page accessible only to authenticated users)
- User Dashboard

## Requirements

- Python 3.x
- Django 5.x

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/trekkali/mon_projet_django.git
    cd mon_projet_django
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000`.

## Usage

### User Registration

1. Go to the signup page: `http://127.0.0.1:8000/signup/`.
2. Fill in the registration form with your details and submit.
3. You will be redirected to the login page upon successful registration.

### User Login

1. Go to the login page: `http://127.0.0.1:8000/login/`.
2. Enter your email and password to log in.
3. Upon successful login, you will be redirected to the dashboard.

### Password Reset

1. Go to the password reset page: `http://127.0.0.1:8000/reset/`.
2. Enter your email to receive password reset instructions.

### Contact Page (Protected View)

1. Ensure you are logged in.
2. Access the contact page: `http://127.0.0.1:8000/contact/`.
3. If you are not logged in, you will be redirected to the login page.

## Project Structure

simple-django-authentication/
│
├── authentification/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│
├── formulaire/
│ ├── migrations/
│ ├── templates/
│ │ ├── contact.html
│ │ ├── dashboard.html
│ │ ├── login.html
│ │ ├── reset.html
│ │ ├── signup.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ ├── views.py
│
├── manage.py
├── requirements.txt
└── README.md

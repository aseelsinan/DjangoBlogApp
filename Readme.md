📝 Premium Django Blogging System

A professional and fully dynamic blogging platform built using Django Framework.
This project demonstrates real-world web development concepts including authentication, user roles, media handling, SEO-friendly URLs, and production deployment.

🚀 Project Overview

This is not a basic blog template — it is a complete blogging system designed with scalability and best practices in mind.

The system supports multiple user roles, secure authentication, dynamic content management, and deployment-ready configuration.

Built to simulate real industry-level blog platforms.

✨ Features

🔐 Authentication System (Login / Logout / Registration)

👥 Role-Based Access Control

Manager: Full control over users and content

Editor: Content management permissions only

📝 Dynamic Post Management (CRUD)

🏷 Category System with ForeignKey Relationships

🔎 SEO-Friendly Slug URLs

💬 Comment System (Login Required)

🖼 Featured Image Upload Support

📅 Post Ordering by Publish Date

📦 Bootstrap Integrated UI

🛠 Django Admin Customization

🌍 Production Deployment Ready (DEBUG=False, SSL Config)

🧠 Technical Stack

Python

Django

SQLite (Development)

Bootstrap

HTML / CSS

Django ORM

Virtual Environment

PythonAnywhere (Deployment)

📂 Database Structure

Category Model

Post Model

Linked via ForeignKey

Slug Field for SEO

Comment Model

Custom User Role Handling

🖼 Media Handling

Configured MEDIA_ROOT and MEDIA_URL

Image upload for blog posts

Proper static files configuration

⚙ Setup Instructions
# Clone the repository
git clone https://github.com/your-username/your-repo-name.git

# Navigate into the project
cd your-repo-name

# Create virtual environment
python -m venv venv

# Activate environment
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver

🌐 Deployment

This project can be deployed on:

PythonAnywhere

Heroku

VPS

Any WSGI-compatible hosting

Make sure to:

Set DEBUG = False

Configure ALLOWED_HOSTS

Set up static & media files properly

🎯 Learning Objectives

This project demonstrates:

Clean Django project structure

MVC (MTV) architecture understanding

ORM relationships

Role-based permission systems

Production-ready configuration

📌 Author

Aseel Sinan
Django Developer 

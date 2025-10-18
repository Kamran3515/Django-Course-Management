# Django Course Management System

This is a **Course Management System** built with **Django REST Framework** and **Docker**, designed to manage courses, students, and teachers.

---

## 🧱 Features

- Role-based access:
  - **Admin**: Manage all courses and users
  - **Teacher**: Create and manage their courses
  - **Student**: Register and enroll in courses
- JWT Authentication using **SimpleJWT**
- REST API endpoints for all operations
- Dockerized environment for easy setup

---

## ⚙️ Requirements

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)
- [Git Desktop](https://desktop.github.com/) (for version control)

---

## 🚀 Setup

### 1. Clone the repository

If you use **Git Desktop**:
1. Open GitHub Desktop
2. File → Clone Repository → Enter the URL of your repository  
3. Choose local path → Clone

Or via command line:
```bash
git clone https://github.com/username/django-course-management.git
cd django-course-management


# 🎓 Django Course Management System

**Django Course Management System** is a learning-based project built with **Django REST Framework**.  
It provides a full backend for managing users, courses, enrollments, lessons, ratings, and comments.  
This project is designed as a **Junior Developer-level** practice for learning how to build structured RESTful APIs.

---

## 🚀 Features

- User authentication with multiple roles (Admin, Teacher, Student)
- Full course management (Create, Update, Delete, View)
- Course categorization by topics
- Student enrollment system
- Lesson management per course
- Rating and comment system
- API documentation via Swagger (drf_yasg / drf-spectacular)
- Token-based authentication
- JWT authentication using `djangorestframework-simplejwt`
- Modular project architecture (accounts, courses, api/v1)
- Docker and PostgreSQL support

---

## 🧱 Project Structure



core/
├── accounts/
│   ├── admin/
│   │   ├── admin_user.py
│   │   └── admin_profile.py
│   ├── models/
│   │   ├── users.py
│   │   └── profiles.py
│   ├───api/v1/
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── permissions.py
│   │
│   ├── urls.py
│   └── views.py
│
├── courses/
│   ├── admin/
│   │   ├── admin_course.py
│   │   ├── admin_lessons.py
│   │   ├── admin_category.py
│   │   ├── admin_comments.py
│   │   ├── admin_enrollment.py
│   │   └── admin_rate.py
│   ├── models/
│   │   ├── course.py
│   │   ├── lessons.py
│   │   ├── category.py
│   │   ├── comments.py
│   │   └── rate.py
│   ├── api/v1/
│   │   ├── serializers/
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── permissions.py
│   └── urls.py
│
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── requirements.txt



---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/Kamran3515/Django-Course-Management.git
cd Django-Course-Management


### 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


### 3. Install dependencies
pip install -r requirements.txt


### 4. Run migrations
python manage.py migrate


### 5. Create a superuser
python manage.py createsuperuser

### 6. Start the development server
python manage.py runserver

---

## 🧭 API Endpoints

| Endpoint               | Description                          | Methods   |
| ---------------------- | ------------------------------------ | --------- |
| `/api/v1/courses/`     | List or manage courses               | GET, POST |
| `/api/v1/enrollments/` | Enroll students in courses           | GET, POST |
| `/api/v1/categories/`  | View course categories               | GET       |
| `/api/v1/comments/`    | Manage course comments               | GET, POST |
| `/api/v1/rates/`       | Rate courses                         | GET, POST |
| `/api/token/`          | Obtain JWT tokens (access & refresh) | POST      |
| `/api/token/refresh/`  | Refresh access token                 | POST      |

---

## 🔑 Authentication (JWT)

This project uses **JWT authentication** via `djangorestframework-simplejwt`.

* To obtain tokens, send your credentials to `/api/token/`
  You’ll receive an `access` and a `refresh` token.
* Include the access token in your requests:

Authorization: Bearer <access_token_here>


* When the access token expires, use `/api/token/refresh/` to get a new one.

---

## 🧪 Testing

# Run all project tests:
python manage.py test

---

## 🐳 Run with Docker (Optional)
docker-compose up --build
# Database credentials are defined in the `.env` file.
# Default configuration uses **PostgreSQL**.

---

## 🧩 Tech Stack

| Component        | Technology                      |
| ---------------- | ------------------------------- |
| Backend          | Django 5, Django REST Framework |
| Database         | PostgreSQL                      |
| Containerization | Docker                          |
| Authentication   | DRF TokenAuth                   |
| Documentation    | drf-yasg (Swagger)              |
| Language         | Python 3.12                     |

---

## 👨‍💻 Developer

Name: Kamran
GitHub: [Kamran3515](https://github.com/Kamran3515)
Goal: To learn RESTful API design and build a structured real-world Django project.

---

## 🏁 Future Improvements

JWT authentication
Course payment and purchase system
React or Next.js frontend dashboard
Advanced search and filtering

---

📘 This project is a learning-based Django REST API example for educational purposes.

---


# Django PostgreSQL CRUD Project

A simple Student Management System built using Django and PostgreSQL. This project demonstrates the implementation of CRUD (Create, Read, Update, Delete) operations using Django ORM.

## Project Overview

The Student Management System allows users to manage student records through a simple web interface. Users can add new students, view existing records, update student information, and delete records.

## Technologies Used

- Python
- Django
- PostgreSQL
- HTML
- Django ORM

## Features

- Add new student records
- View all student records
- Update existing student details
- Delete student records
- Form validation using Django ModelForm
- PostgreSQL database integration
- Simple and user-friendly interface

## Project Structure

```text
Django-PostgreSQL-CRUD/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── students/
│   ├── migrations/
│   ├── templates/
│   │   └── students/
│   │       ├── student_list.html
│   │       ├── student_form.html
│   │       └── student_confirm_delete.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
└── README.md
```

## Database Configuration

This project uses PostgreSQL as its database.

Database details:

- Database Name: student_db
- Database User: postgres
- Host: localhost
- Port: 5432

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Django-PostgreSQL-CRUD.git
```

### 2. Navigate to the Project Folder

```bash
cd Django-PostgreSQL-CRUD
```

### 3. Create a Virtual Environment

```bash
python -m venv env
```

### 4. Activate Virtual Environment

Windows:

```bash
env\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure PostgreSQL

- Install PostgreSQL and pgAdmin.
- Create a database named `student_db`.
- Configure database credentials in `config/settings.py`.

### 7. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open your browser:

http://127.0.0.1:8000/

## CRUD Operations

| Operation | Description |
|---|---|
| Create | Add new student records |
| Read | Display all student records |
| Update | Modify existing student details |
| Delete | Remove student records |

## Learning Outcomes

- Understanding Django MVT architecture
- Working with Django Models and ModelForm
- Understanding Django ORM queries
- Connecting Django with PostgreSQL
- Implementing CRUD operations
- Handling HTML forms and HTTP requests
- Working with Django migrations

## Future Improvements

- Add student search functionality
- Add pagination
- Improve UI using Bootstrap
- Implement user authentication

## Author

Sumit Todkar

## License

This project is created for learning and educational purposes.

# Student Management API

A REST API built with **FastAPI**, **SQLAlchemy**, **SQLite**, and **Pydantic** to manage student records.

## Features

- Create new student records
- Retrieve all students or a student by ID
- Update student details
- Delete student records
- Search students by name or course
- Pagination with `skip` and `limit`
- Sort students by ID, name, or age
- Input validation and interactive API documentation

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## Project Structure

```text
student-management-api/
├── app/
│   ├── routes/
│   │   └── student.py
│   ├── database.py
│   ├── model.py
│   └── schemas.py
├── main.py
├── requirements.txt
└── .gitignore
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/prakashtamanna6937-a11y/student-management-api.git
cd student-management-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment on Windows

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the API

```bash
python -m uvicorn main:app --reload
```

### 6. Open the API documentation

Visit http://127.0.0.1:8000/docs in your browser.

## Main API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/students/` | Create a student |
| GET | `/students/` | List students with pagination and sorting |
| GET | `/students/search/` | Search by name or course |
| GET | `/students/{student_id}` | Get a student by ID |
| PUT | `/students/{student_id}` | Update a student |
| DELETE | `/students/{student_id}` | Delete a student |

## Learning Project

This project was developed to practice REST API development, database integration, CRUD operations, request validation, searching, pagination, and sorting.

## Author

Tamanna Prakash
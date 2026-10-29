
from fastapi import FastAPI

from app.database import Base, engine
from app import model
from app.routes import student

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management API",
    description="An API to manage student records",
    version="1.0.0"
)

app.include_router(student.router)


@app.get("/")
def home():
    return {
        "message": "Welcome to the Student Management API!"
    }

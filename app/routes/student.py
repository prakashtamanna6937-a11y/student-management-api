
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.model import Student
from app.schemas import StudentCreate, StudentResponse

router = APIRouter(prefix="/students", tags=["Students"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    existing_student = (
        db.query(Student)
        .filter(Student.email == student.email)
        .first()
    )

    if existing_student:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_student = Student(**student.model_dump())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student



@router.get("/", response_model=list[StudentResponse])
def get_students(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100),
    sort_by: str = Query(default="id", pattern="^(id|name|age)$"),
    db: Session = Depends(get_db)
):
    query = db.query(Student)

    if sort_by == "name":
        query = query.order_by(Student.name)
    elif sort_by == "age":
        query = query.order_by(Student.age)
    else:
        query = query.order_by(Student.id)

    return query.offset(skip).limit(limit).all()


@router.get("/search/", response_model=list[StudentResponse])
def search_students(
    name: str | None = Query(default=None, min_length=1, max_length=100),
course: str | None = Query(default=None, min_length=1, max_length=100),
    db: Session = Depends(get_db)
):
    query = db.query(Student)

    if name:
        query = query.filter(Student.name.ilike(f"%{name}%"))

    if course:
        query = query.filter(Student.course.ilike(f"%{course}%"))

    return query.all()

@router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


@router.put("/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    student_data: StudentCreate,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(Student.id == student_id).first()

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    existing_email = (
        db.query(Student)
        .filter(
            Student.email == student_data.email,
            Student.id != student_id
        )
        .first()
    )

    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")

    student.name = student_data.name
    student.age = student_data.age
    student.course = student_data.course
    student.email = student_data.email

    db.commit()
    db.refresh(student)

    return student


@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()

    return {"message": "Student deleted successfully"}




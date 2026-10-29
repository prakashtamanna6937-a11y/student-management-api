
from pydantic import BaseModel, EmailStr, Field


class StudentCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(gt=0, le=120)
    course: str = Field(min_length=1, max_length=100)
    email: EmailStr


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    course: str
    email: EmailStr

    class Config:
        from_attributes = True

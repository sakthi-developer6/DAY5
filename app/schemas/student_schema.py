from pydantic import BaseModel, EmailStr, Field


class StudentCreate(BaseModel):

    name: str = Field(..., min_length=3, max_length=100)

    age: int = Field(..., gt=0, lt=100)

    department: str

    email: EmailStr


class StudentResponse(StudentCreate):

    id: int

    class Config:
        from_attributes = True
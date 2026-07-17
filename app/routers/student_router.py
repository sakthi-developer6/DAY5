from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.student_schema import StudentCreate
from app.schemas.student_schema import StudentResponse

from app.services import student_service

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.post(
    "/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def add_student(student: StudentCreate, db: Session = Depends(get_db)):

    return student_service.create_student(db, student)


@router.get(
    "/",
    response_model=list[StudentResponse]
)
def get_all_students(db: Session = Depends(get_db)):

    return student_service.get_students(db)
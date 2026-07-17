from fastapi import FastAPI

from app.database.connection import Base
from app.database.connection import engine

from app.routers.student_router import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management API",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "Welcome to Student Management System"
    }
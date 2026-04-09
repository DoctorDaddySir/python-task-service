from fastapi import APIRouter
from app.services.task_service import TaskService

router = APIRouter()
service = TaskService()


@router.get("/")
def root():
    return {"message": "Task Service is running"}


@router.post("/tasks")
def create_task(name: str):
    return service.create_task(name)


@router.get("/tasks")
def get_tasks():
    return service.get_all_tasks()
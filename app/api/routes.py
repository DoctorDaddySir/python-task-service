from fastapi import APIRouter
from app.services.task_service import TaskService
from app.config import settings

router = APIRouter()
service = TaskService()


@router.get("/")
def root():
    return {
        "message": f"{settings.service_name} is running",
        "environment": settings.environment
    }


@router.post("/tasks")
def create_task(name: str):
    return service.create_task(name)


@router.get("/tasks")
def get_tasks():
    return service.get_all_tasks()
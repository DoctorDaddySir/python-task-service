from app.repositories.task_repository import TaskRepository


class TaskService:
    def __init__(self):
        self.repo = TaskRepository()

    def create_task(self, name: str):
        return self.repo.create(name)

    def get_all_tasks(self):
        return self.repo.get_all()
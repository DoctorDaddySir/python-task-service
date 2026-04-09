import uuid


class TaskRepository:
    def __init__(self):
        self.tasks = []

    def create(self, name: str):
        task = {
            "id": str(uuid.uuid4()),
            "name": name,
            "status": "pending"
        }
        self.tasks.append(task)
        return task

    def get_all(self):
        return self.tasks
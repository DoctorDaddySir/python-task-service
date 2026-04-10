import os


class Settings:
    def __init__(self):
        self.service_name = os.getenv("SERVICE_NAME", "Task Service")
        self.environment = os.getenv("ENVIRONMENT", "development")


settings = Settings()
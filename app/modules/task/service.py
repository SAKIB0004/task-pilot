from app.modules.task.repository import TaskRepository


class TaskService:

    def __init__(self) -> None:
        self.repo = TaskRepository()

    def create_task(self, body):

        return self.repo.create(body.model_dump(exclude_unset=True))
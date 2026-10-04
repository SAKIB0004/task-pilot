from app.db.session_manager import SessionManager
from app.modules.task.model import Task


class TaskRepository:
    def __init__(self):
        self.session_manager = SessionManager()

    def create(self, payload):
        task = Task(**payload)

        with self.session_manager.get_db_session() as session:
            session.add(task)
            session.commit()
            session.refresh(task)

        return task 
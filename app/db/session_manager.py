from collections.abc import Generator
from contextlib import contextmanager

from sqlalchemy.orm import Session

from app.db.session import SessionLocal


class SessionManager:
    """Manage database session lifecycle."""

    @staticmethod
    @contextmanager
    def get_db_session() -> Generator[Session, None, None]:
        session = SessionLocal()

        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
from sqlalchemy import DateTime, Index, String, Text, func, Column, Integer

from app.db.base import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(String(50), primary_key=True)
    user_id = Column(String(50), nullable=True)
    title = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    status = Column(String(50), nullable=False, default="pending")
    priority = Column(String(50), nullable=False, default="medium") 
    due_date = Column(DateTime(timezone=False), nullable=True)

    created_at = Column(DateTime(timezone=False), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=False), nullable=False, server_default=func.now(), onupdate=func.now())


    __table_args__ = (
        Index("ix_tasks_user_status", "user_id", "status"),
        Index("ix_tasks_user_priority", "user_id", "priority"),
        Index("ix_tasks_user_due_date", "user_id", "due_date"),
    )
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.modules.task.enums import TaskPriority, TaskStatus


class FilterParams(BaseModel):
    status: TaskStatus | None = None

    priority: TaskPriority | None = None

    search: str | None = Field(
        default=None,
        min_length=1,
        max_length=255,
    )

    due_from: datetime | None = None
    due_to: datetime | None = None

    created_from: datetime | None = None
    created_to: datetime | None = None

    model_config = ConfigDict(
        extra="forbid",
    )
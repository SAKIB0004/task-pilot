from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field
from enum import Enum
from typing import Optional
from app.utils.pagination import PaginationMeta

class TaskPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class TaskBase(BaseModel):
    title: str = Field(..., min_length=1,max_length=255)
    description: Optional[str] = Field(default=None, max_length=5000)
    priority: TaskPriority 
    due_date: datetime

    model_config = ConfigDict(from_attributes=True)

class TaskCreateBody(TaskBase):
    user_id: str = Field(..., min_length=1, max_length=50)
    

class TaskUpdateBody(TaskBase):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None
    due_date: Optional[datetime] = None

    model_config = ConfigDict(extra="forbid")

class TaskResponseItem(TaskBase):
    id: int
    user_id: str 
    status: TaskStatus
    created_at: datetime
    updated_at: datetime

 
class TaskCreateResponse(BaseModel):
    status: str = "success"
    data: TaskResponseItem

class TaskUpdateResponse(BaseModel):
    status: str = "success"
    data: TaskResponseItem

class TaskGetResponse(BaseModel):
    status: str = "success"
    data: TaskResponseItem

TaskListData = PaginationMeta[TaskResponseItem]

class TaskListResponse(BaseModel):
    status: str = "success"
    data: TaskListData  
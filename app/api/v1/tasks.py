from typing import Annotated

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.modules.task.schemas import (
    TaskCreateBody, TaskCreateResponse
)
from app.modules.task.service import TaskService

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)



@router.post(
    "",
    response_model=TaskCreateResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    body: TaskCreateBody,
):
    obj = TaskService().create_task(body)
    return TaskCreateResponse(status="success", data=obj)
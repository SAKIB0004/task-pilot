from fastapi import APIRouter

from app.api.v1.chat import router as chat_router
from app.api.v1.health import router as health_router
from app.api.v1.tasks import router as tasks_router
from app.core.config import get_settings

settings = get_settings()

api_router = APIRouter()

api_router.include_router(health_router)
api_router.include_router(tasks_router)
api_router.include_router(chat_router)
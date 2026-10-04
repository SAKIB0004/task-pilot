from fastapi import FastAPI

from app.api.v1 import api_router
from app.core.config import get_settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import configure_logging

settings = get_settings()

configure_logging()


def create_application():
    app = FastAPI(
        title=settings.app_name,
        description="AI-powered task management REST API.",
        version="1.0.0",
        debug=settings.debug,
    )

    app.include_router(
        api_router,
        prefix="/api/v1",
    )

    register_exception_handlers(app)

    return app


app = create_application()
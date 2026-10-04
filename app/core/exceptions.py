from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class AppException(Exception):
    """Base application exception."""

    status_code: int = 500
    code: str = "internal_error"
    message: str = "An unexpected error occurred."

    def __init__(self, message: str | None = None, *, status_code: int | None = None, code: str | None = None) -> None:
        self.message = message or self.message
        self.status_code = status_code or self.status_code
        self.code = code or self.code

        super().__init__(self.message)


async def app_exception_handler(request: Request, exc: AppException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "details": {
                "code": exc.code,
                "message": exc.message,
            },
        },
    )


async def unhandled_exception_handler(request: Request, exc: Exception,) -> JSONResponse:
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "details": {
                "code": "internal_error",
                "message": "An unexpected error occurred.",
            },
        },
    )


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(AppException, app_exception_handler)

    app.add_exception_handler(Exception, unhandled_exception_handler)
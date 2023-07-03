from fastapi import FastAPI

from .post import router as post_router
from .exceptions import setup_exception_handlers


def setup_controllers(app: FastAPI) -> None:
    app.include_router(router=post_router)
    setup_exception_handlers(app=app)

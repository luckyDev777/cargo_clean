from fastapi import FastAPI

from .post import router as post_router


def setup_controllers(app: FastAPI) -> None:
    app.include_router(router=post_router)

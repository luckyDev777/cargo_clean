from fastapi import FastAPI
from .test import router as test_router


def setup_controllers(app: FastAPI) -> None:
    app.include_router(test_router)

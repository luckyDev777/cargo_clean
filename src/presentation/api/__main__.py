import uvicorn
from fastapi import FastAPI

from .main import build_app
from .settings.config import load_config


def main() -> FastAPI:
    config_ = load_config()

    app = build_app(config=config_)

    return app

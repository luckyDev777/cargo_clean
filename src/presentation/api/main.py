import uvicorn

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from .settings.config import APIConfig, Config
from .controllers.main import setup_controllers
from .di.main import setup_di
from .lifespan import lifespan
from ...adapters.sentry.main import setup_sentry


# uvicorn wsgi/asgi

def build_app(config: Config) -> FastAPI:
    app = FastAPI(title="Cargo", default_response_class=ORJSONResponse, lifespan=lifespan)

    # Configuration Block
    setup_controllers(app=app)
    setup_di(app=app, config=config)

    setup_sentry(config=config.sentry)

    return app

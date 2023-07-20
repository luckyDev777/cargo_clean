import pytest_asyncio
from asgi_lifespan import LifespanManager
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.adapters.cache.config import CacheConfig
from src.adapters.db.config import DBConfig
from src.presentation.api.controllers.main import setup_controllers
from src.presentation.api.di.main import setup_di
from src.presentation.api.settings.config import Config, APIConfig


def get_test_config() -> Config:
    return Config(
        api=APIConfig(),
        db=DBConfig(
            db_port=5432,
            db_password="postgres",
            db_user="postgres",
            db_name="postgres",
            db_host="test_db"
        ),
        sentry=None,
        cache=CacheConfig(
            host="test_cache",
            port=6379
        )
    )


async def build_test_integration_app(config: Config) -> FastAPI:
    from src.presentation.api.lifespan import lifespan

    app = FastAPI(title="Cargo", default_response_class=ORJSONResponse, lifespan=lifespan)
    # Configuration Block
    setup_controllers(app=app)
    setup_di(app=app, config=config)

    return app


@pytest_asyncio.fixture(scope="session")
async def get_test_integration_app() -> FastAPI:
    config_ = get_test_config()

    app = await build_test_integration_app(config=config_)

    async with LifespanManager(app=app) as manager:
        yield app

import os
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.adapters.db.main import create_engine, session_factory
from src.presentation.api.settings.config import load_config
from tests.mocks import get_test_config


@asynccontextmanager
async def lifespan(app: FastAPI):
    if os.getenv("TEST"):
        config = get_test_config()
    else:
        config = load_config()
    engine = create_engine(db_config=config.db)
    pool = session_factory(engine=engine)

    app.state.engine = engine
    app.state.pool = pool

    yield

    await app.state.engine.dispose()

    del app.state.engine

import asyncio
from typing import AsyncGenerator, Any, Generator

import pytest
import pytest_asyncio
from asgi_lifespan import LifespanManager
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine
from sqlalchemy.orm import close_all_sessions

from src.adapters.db.models import Post
from tests.mocks import get_test_integration_app, get_test_config, build_test_integration_app


@pytest.fixture(scope="session")
def event_loop() -> Generator:
    loop = asyncio.get_event_loop_policy().get_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="session")
async def get_test_integration_app() -> FastAPI:
    config_ = get_test_config()

    app = await build_test_integration_app(config=config_)

    async with LifespanManager(app=app) as manager:
        yield app


@pytest_asyncio.fixture(scope="session")
async def integration_client(get_test_integration_app) -> AsyncGenerator[AsyncClient, Any]:
    async with AsyncClient(app=get_test_integration_app, base_url="http://test") as client:
        yield client


@pytest_asyncio.fixture(scope="session")
async def db_session_test() -> async_sessionmaker[AsyncSession]:
    engine = create_async_engine(url="postgresql+asyncpg://postgres:postgres@test_db:5432/postgres")
    session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
        bind=engine, expire_on_commit=False, autoflush=False
    )
    yield session_factory
    await engine.dispose()


@pytest_asyncio.fixture(scope="session")
async def session(db_session_test: async_sessionmaker[AsyncSession]) -> AsyncGenerator[AsyncSession, Any]:
    async with db_session_test() as session_test:
        yield session_test
    close_all_sessions()


@pytest.fixture(scope="function")
def post_data() -> dict:
    return {
        "post_id": 1,
        "post_name": "Не люблю писать тесты"
    }


@pytest_asyncio.fixture(scope="session")
async def create_posts_in_db(session: AsyncSession):
    async def create_posts_in_db_with_args(post_id: int, post_name: str):
        statement = insert(Post).values(id=post_id, name=post_name)
        await session.execute(statement)
        await session.commit()

    return create_posts_in_db_with_args

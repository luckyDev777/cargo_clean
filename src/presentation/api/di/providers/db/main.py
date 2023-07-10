from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, AsyncSession

from src.adapters.db.config import DBConfig
from src.adapters.db.main import create_engine, session_factory, build_session
from src.presentation.api.di.stub import Stub


def session_factory_provider(engine: AsyncEngine = Depends(Stub(AsyncEngine))) -> async_sessionmaker[AsyncSession]:
    return session_factory(engine=engine)


async def session_provider(
        pool: async_sessionmaker[AsyncSession] = Depends(Stub(async_sessionmaker[AsyncSession]))
) -> AsyncSession:
    async with build_session(pool) as session:
        yield session

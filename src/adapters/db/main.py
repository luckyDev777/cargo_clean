# Фабрики, которые либо будут переиспользоваться, либо будут один раз инициализированы один раз где-то И ВСЕ.(main)
# Фабрика - порождающий паттерн, который нужен для того, чтобы управлять созданием объекта
# инициализация один раз пример, как избежать глобалы
import contextlib
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine, AsyncSession

from .config import DBConfig


# engine - держит подключение к БД
# Организация адаптера DB, организация presentation(api)

@contextlib.asynccontextmanager
async def create_engine(db_config: DBConfig) -> AsyncEngine:
    engine = create_async_engine(db_config.full_url, echo=db_config.db_echo)

    yield engine

    await engine.dispose()


def session_factory(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


@contextlib.asynccontextmanager
async def build_session(
        factory: async_sessionmaker[AsyncSession],
) -> AsyncGenerator[AsyncSession, None]:
    async with factory() as session:
        yield session

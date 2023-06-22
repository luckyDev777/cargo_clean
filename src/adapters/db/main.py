# Фабрики, которые либо будут переиспользоваться, либо будут один раз инициализированы один раз где-то И ВСЕ.(main)
# Фабрика - порождающий паттерн, который нужен для того, чтобы управлять созданием объекта
# инициализация один раз пример, как избежать глобалы
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine, AsyncSession

from .config import DBConfig


# Организация адаптера DB, организация presentation(api)
def create_engine(db_config: DBConfig) -> AsyncEngine:
    return create_async_engine(db_config.full_url, echo=db_config.echo)


def session_factory(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(
        bind=engine,
        autoflush=False,
        expire_on_commit=False
    )

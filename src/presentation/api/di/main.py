from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.business_logic.common.interfaces.persistance.uow import UoW
from src.business_logic.post.interfaces.dao import PostDAO
from .providers.db.main import DBProvider
from .stub import Stub
from ..settings.config import Config


def setup_di(app: FastAPI, config: Config, pool: async_sessionmaker[AsyncSession]) -> None:
    db_provider = DBProvider(pool=pool)

    app.dependency_overrides[Stub(PostDAO)] = db_provider.post_dao
    app.dependency_overrides[Stub(UoW)] = db_provider.uow

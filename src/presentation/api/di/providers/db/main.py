from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from src.adapters.db.dao.post import PostDAOImpl
from src.adapters.db.uow import SQLAlchemyUoW
from src.business_logic.common.interfaces.persistance.uow import UoW
from src.business_logic.post.interfaces.dao import PostDAO


class DBProvider:
    def __init__(self, pool: async_sessionmaker[AsyncSession]):
        self._pool = pool

    async def post_dao(self) -> PostDAO:
        async with self._pool() as session:
            yield PostDAOImpl(session=session)

    async def uow(self) -> UoW:
        async with self._pool() as session:
            yield SQLAlchemyUoW(session=session)

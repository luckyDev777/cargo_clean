from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from src.adapters.db.dao.post import PostDAOImpl
from src.business_logic.post.interfaces.dao import PostDAO


class DBProvider:
    def __init__(self, pool: async_sessionmaker[AsyncSession]):
        self._pool = pool

    async def post_dao(self) -> PostDAO:
        async with self._pool() as session:
            yield PostDAOImpl(session=session)

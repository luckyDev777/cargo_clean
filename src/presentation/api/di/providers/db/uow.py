from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.adapters.db.dao.post import PostDAOImpl
from src.adapters.db.uow import SQLAlchemyUoW
from src.business_logic.common.interfaces.persistance.uow import UoW
from src.business_logic.post.interfaces.dao import PostDAO
from src.presentation.api.di.stub import Stub


def uow_provider(session: Annotated[AsyncSession, Depends(Stub(AsyncSession))]) -> UoW:
    return SQLAlchemyUoW(session=session)


def post_dao_provider(session: Annotated[AsyncSession, Depends(Stub(AsyncSession))]) -> PostDAO:
    return PostDAOImpl(session=session)

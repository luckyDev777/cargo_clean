from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, AsyncEngine

from src.adapters.db.config import DBConfig
from src.business_logic.common.interfaces.persistance.uow import UoW
from src.business_logic.post.interfaces.dao import PostDAO
from src.business_logic.post.services import CreatePostService, GetPostService, GetAllPostsService
from .providers.db.main import session_factory_provider, session_provider
from .providers.db.uow import uow_provider, post_dao_provider
from .providers.services.post import create_post_service, get_post_service, get_posts_service
from .stub import Stub
from ..settings.config import Config


def setup_di(app: FastAPI, config: Config) -> None:
    # Setup DB dependencies
    app.dependency_overrides[Stub(AsyncEngine)] = lambda: app.state.engine
    app.dependency_overrides[Stub(async_sessionmaker[AsyncSession])] = lambda: app.state.pool
    app.dependency_overrides[Stub(AsyncSession)] = session_provider
    app.dependency_overrides[Stub(UoW)] = uow_provider
    app.dependency_overrides[Stub(PostDAO)] = post_dao_provider

    # Setup services
    app.dependency_overrides[Stub(CreatePostService)] = create_post_service
    app.dependency_overrides[Stub(GetPostService)] = get_post_service
    app.dependency_overrides[Stub(GetAllPostsService)] = get_posts_service

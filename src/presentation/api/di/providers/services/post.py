from typing import Annotated

from fastapi import Depends

from src.business_logic.common.interfaces.persistance.uow import UoW
from src.business_logic.post.interfaces.cache import CacheDAO
from src.business_logic.post.interfaces.dao import PostDAO
from src.business_logic.post.services import GetPostService, CreatePostService, GetAllPostsService, UpdatePostService, \
    DeletePostService
from src.presentation.api.di.stub import Stub


def get_posts_service(
        dao: PostDAO = Depends(Stub(PostDAO)),
        cache_dao: CacheDAO = Depends(Stub(CacheDAO))
) -> GetAllPostsService:
    return GetAllPostsService(dao=dao, cache_dao=cache_dao)


def get_post_service(dao: PostDAO = Depends(Stub(PostDAO))) -> GetPostService:
    return GetPostService(dao=dao)


def create_post_service(
        uow: Annotated[UoW, Depends(Stub(UoW))],
        dao: Annotated[PostDAO, Depends(Stub(PostDAO))],
        cache: Annotated[CacheDAO, Depends(Stub(CacheDAO))]
) -> CreatePostService:
    return CreatePostService(dao=dao, uow=uow, cache=cache)


def update_post_service(
        uow: Annotated[UoW, Depends(Stub(UoW))],
        dao: Annotated[PostDAO, Depends(Stub(PostDAO))]
) -> UpdatePostService:
    return UpdatePostService(dao=dao, uow=uow)


def delete_post_service(
        uow: Annotated[UoW, Depends(Stub(UoW))],
        dao: Annotated[PostDAO, Depends(Stub(PostDAO))]
) -> DeletePostService:
    return DeletePostService(uow=uow, dao=dao)

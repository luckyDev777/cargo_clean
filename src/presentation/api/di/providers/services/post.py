from fastapi import Depends

from src.business_logic.common.interfaces.persistance.uow import UoW
from src.business_logic.post.interfaces.dao import PostDAO
from src.business_logic.post.services import GetPostService, CreatePostService
from src.presentation.api.di.stub import Stub


def get_post_service(dao: PostDAO = Depends(Stub(PostDAO))) -> GetPostService:
    return GetPostService(dao=dao)


def create_post_service(
        dao: PostDAO = Depends(Stub(PostDAO)),
        uow: UoW = Depends(Stub(UoW))
) -> CreatePostService:
    return CreatePostService(dao=dao, uow=uow)

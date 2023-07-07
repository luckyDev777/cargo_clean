from typing import Annotated

from fastapi import Depends

from src.business_logic.common.interfaces.persistance.uow import UoW
from src.business_logic.post.interfaces.dao import PostDAO
from src.business_logic.post.services import GetPostService, CreatePostService
from src.presentation.api.di.stub import Stub


def create_post_service(
        uow: Annotated[UoW, Depends(Stub(UoW))],
        dao: Annotated[UoW, Depends(Stub(PostDAO))]
) -> CreatePostService:
    return CreatePostService(dao=dao, uow=uow)

from typing import Annotated

from fastapi import APIRouter, status, Depends

from src.business_logic.common.interfaces.persistance.uow import UoW
from src.business_logic.post import dto
from src.business_logic.post.services.create_post import CreatePostService
from src.presentation.api.di.stub import Stub

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post(
    path="/",
    responses={
        status.HTTP_201_CREATED: {"model": dto.Post}
    }
)
async def create_post(
        post_info: dto.CreatePost,
        service: Annotated[CreatePostService, Depends(Stub(CreatePostService))]
) -> dto.Post:
    return await service(post_info=post_info)

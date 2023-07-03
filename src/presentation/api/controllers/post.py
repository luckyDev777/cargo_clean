from fastapi import APIRouter, status, Depends

from src.business_logic.post import dto
from src.business_logic.post.services.get_post import GetPostService
from src.presentation.api.di.providers.services.post import get_post_service
from src.presentation.api.controllers.responses import ErrorResult
from src.business_logic.post.exceptions import PostIdNotExists

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get(
    path='/{post_id}',
    responses={
        status.HTTP_200_OK: {"model": dto.Post},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResult[PostIdNotExists]},
    },
)
async def get_post_by_id(
        post_id: int,
        service: GetPostService = Depends(get_post_service)
) -> dto.Post:
    return await service(dto.GetPost(post_id=post_id))

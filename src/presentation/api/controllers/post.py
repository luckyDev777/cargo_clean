from fastapi import APIRouter, status, Depends

from src.business_logic.post import dto
from src.business_logic.post.services.create_post import CreatePostService
from src.business_logic.post.services.get_post import GetPostService
from src.presentation.api.di.providers.services.post import get_post_service, create_post_service

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get(
    path='/{post_id}',
    responses={
        status.HTTP_200_OK: {"model": dto.Post}
    },
)
async def get_post_by_id(
        post_id: int,
        service: GetPostService = Depends(get_post_service)
) -> dto.Post:
    return await service(dto.GetPost(post_id=post_id))


@router.post(
    path="/",
    responses={
        status.HTTP_201_CREATED: {"model": dto.Post}
    }
)
async def create_post(
        post_data: dto.CreatePost,
        service: CreatePostService = Depends(create_post_service)
) -> dto.Post:
    return await service(post_info=post_data)



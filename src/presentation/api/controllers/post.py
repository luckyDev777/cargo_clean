import asyncio
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from typing import Annotated, Type, Generator, BinaryIO, Any

from fastapi import APIRouter, Response, status, Depends
from fastapi.responses import ORJSONResponse, FileResponse, StreamingResponse
from pydantic import BaseModel
from starlette.concurrency import run_in_threadpool

from src.business_logic.post import dto
from src.business_logic.post.services.create_post import CreatePostService
from src.business_logic.post.services.get_post import GetPostService
from src.business_logic.post.services.get_all_posts import GetAllPostsService
from src.business_logic.post.services.update_post import UpdatePostService
from src.business_logic.post.services.delete_post import DeletePostService
from src.presentation.api.controllers import requests
from src.presentation.api.controllers.responses.post import EmptyBodyResponse

from src.presentation.api.di.stub import Stub
from src.presentation.api.controllers.responses import ErrorResult
from src.business_logic.post.exceptions import PostIdNotExists

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get(
    path='/',
    responses={
        status.HTTP_200_OK: {"model": list[dto.Post]}
    },
)
async def get_posts(
        service: Annotated[GetAllPostsService, Depends(Stub(GetAllPostsService))]
) -> list[dto.Post]:
    return await service()


@router.get(
    path='/{post_id}',
    responses={
        status.HTTP_200_OK: {"model": dto.Post},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResult[PostIdNotExists]},
    },
)
async def get_post_by_id(
        post_id: int,
        service: Annotated[GetPostService, Depends(Stub(GetPostService))]
) -> dto.Post:
    return await service(dto.GetPost(post_id=post_id))


@router.post(
    path="/create",
    responses={
        status.HTTP_201_CREATED: {"model": dto.Post}
    }
)
async def create_post(
        post_info: dto.CreatePost,
        service: Annotated[CreatePostService, Depends(Stub(CreatePostService))]
) -> dto.Post:
    return await service(post_info=post_info)


@router.patch(
    path="/{post_id}",
    responses={
        status.HTTP_201_CREATED: {"model": dto.Post},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResult[PostIdNotExists]},
    }
)
async def update_post(
        post_id: int,
        post_info: requests.UpdatePostRequest,
        service: Annotated[UpdatePostService, Depends(Stub(UpdatePostService))]
) -> dto.Post:
    return await service(post_id=post_id, post_info=dto.UpdatePost(name=post_info.name))


@router.delete(
    path="/{post_id}",
    responses={
        status.HTTP_404_NOT_FOUND: {"model": ErrorResult[PostIdNotExists]},
        status.HTTP_204_NO_CONTENT: {"model": None}
    }
)
async def delete_post(
        post_id: int,
        service: Annotated[DeletePostService, Depends(Stub(DeletePostService))]
) -> EmptyBodyResponse:
    await service(post_id=post_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# FileResponse, StreamingResponse

@router.get(
    path="/images/{filename}",
    responses={
        status.HTTP_404_NOT_FOUND: {"model": ErrorResult[PostIdNotExists]}
    }
)
async def get_image(
        filename: str
) -> FileResponse:
    return FileResponse(
        path=f"images/{filename}",
        filename=filename,
        media_type="image/png"
    )


def get_generator(file_path: str) -> Generator[BinaryIO, Any, None]:
    with open(f"images/{file_path}", "rb") as file:
        yield from file


@router.get(
    path="/images_stream/{filename}",
    summary="Короткое описание",
    description="Полное описание",
    responses={
        status.HTTP_404_NOT_FOUND: {"model": ErrorResult[PostIdNotExists]}
    }
)
async def get_image(
        filename: str
) -> StreamingResponse:
    return StreamingResponse(
        get_generator(file_path=filename), media_type="image/png"
    )


def some() -> None:
    time.sleep(10)


@router.get(
    path="/test-io/",
    summary="Короткое описание",
    description="Полное описание",
)
async def get_image(
) -> str:
    #
    # [1, 2, 3, 4, 5, 6]
    # await run_in_threadpool(some) - создает новый? ThreadPoolExecutor
    # await asyncio.to_thread(some) - системный тред пул - _global_execute - PoolThreads
    loop = await asyncio.get_event_loop().run_in_executor(executor=ProcessPoolExecutor(), func=some)
    return "stringsome"

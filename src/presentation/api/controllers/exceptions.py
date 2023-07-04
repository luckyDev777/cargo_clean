from fastapi import FastAPI, status, Request
from fastapi.responses import ORJSONResponse

from src.business_logic.common.exceptions.base import AppException
from src.business_logic.post.exceptions import PostIdNotExists
from src.presentation.api.controllers.responses.exceptions import ErrorResult


def setup_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(PostIdNotExists, post_id_not_exist_handler)
    app.add_exception_handler(Exception, unknown_exception_handler)


async def post_id_not_exist_handler(request: Request, err: PostIdNotExists) -> ORJSONResponse:
    return await handle_error(request, err, status_code=status.HTTP_404_NOT_FOUND)


async def unknown_exception_handler(request: Request, err: Exception) -> ORJSONResponse:
    return ORJSONResponse(
        ErrorResult(message="Unknown server error has occurred", data=err),
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


async def handle_error(request: Request, err: AppException, status_code: int) -> ORJSONResponse:
    return ORJSONResponse(
        ErrorResult(message=err.message, data=err),
        status_code=status_code,
    )

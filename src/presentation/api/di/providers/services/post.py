from fastapi import Depends

from src.business_logic.post.interfaces.dao import PostDAO
from src.business_logic.post.services.get_post import GetPostService
from src.presentation.api.di.stub import Stub


def get_post_service(dao: PostDAO = Depends(Stub(PostDAO))) -> GetPostService:
    return GetPostService(dao=dao)

from src.business_logic.post import dto
from src.business_logic.post.interfaces.dao import PostDAO


class GetPostService:
    def __init__(self, dao: PostDAO) -> None:
        self._dao = dao

    async def __call__(self, post_info: dto.GetPost) -> dto.Post:
        post = await self._dao.get_by_id(post_id=post_info.post_id)
        return post

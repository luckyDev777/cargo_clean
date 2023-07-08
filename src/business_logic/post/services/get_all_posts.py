from src.business_logic.post import dto
from src.business_logic.post.interfaces.dao import PostDAO


class GetAllPostsService:
    def __init__(self, dao: PostDAO) -> None:
        self._dao = dao

    async def __call__(self) -> list[dto.Post]:
        posts = await self._dao.get_posts()
        return posts
import json

from src.business_logic.post import dto
from src.business_logic.post.interfaces.cache import CacheDAO
from src.business_logic.post.interfaces.dao import PostDAO


class GetAllPostsService:
    def __init__(self, dao: PostDAO, cache_dao: CacheDAO) -> None:
        self._dao = dao
        self._cache = cache_dao

    async def __call__(self) -> list[dto.Post]:
        if posts := await self._cache.get_posts(key="posts"):
            exists = json.loads(posts)
            return [dto.Post(post_id=int(key), name=value) for key, value in exists.items()]
        posts = await self._dao.get_posts()
        await self._cache.set_posts(key="posts", value=posts)
        return posts

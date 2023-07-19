import json

from redis.asyncio.client import Redis
from dataclasses import asdict
from src.business_logic.post import dto
from src.business_logic.post.interfaces.cache import CacheDAO


class CacheDAOImpl(CacheDAO):
    def __init__(self, cache_client: Redis) -> None:
        self.client = cache_client

    async def get_posts(self, key: str) -> list[dto.Post]:
        return await self.client.get(name=key)

    async def set_posts(self, key: str, value: list[dto.Post], ex: int | None = None) -> None:
        v = {}

        for a in value:
            v[a.post_id] = a.name

        if ex:
            await self.client.set(name=key, value=json.dumps(v), ex=ex)
            return
        await self.client.set(name=key, value=json.dumps(v))

    async def del_posts(self, key: str):
        await self.client.delete(key)

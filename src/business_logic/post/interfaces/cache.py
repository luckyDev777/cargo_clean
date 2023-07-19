from typing import Protocol

from src.business_logic.post import dto


class CacheDAO(Protocol):

    async def get_posts(self, key: str) -> list[dto.Post]:
        ...

    async def set_posts(self, key: str, value: str, ex: int | None = None) -> None:
        ...

from typing import Protocol

from src.business_logic.post import dto


class PostDAO(Protocol):

    async def get_by_id(self, *, post_id: int) -> dto.Post:
        ...

    async def create_post(self, *, post_name: str) -> dto.Post:
        ...

from typing import Protocol

from src.business_logic.post import dto


class PostDAO(Protocol):

    async def get_by_id(self, *, post_id: int) -> dto.Post:
        ...

    async def create_post(self, *, post_name: str) -> dto.Post:
        ...

    async def get_posts(self) -> list[dto.Post]:
        ...

    async def update_post(self, *, post_id: int, post_info: dto.UpdatePost) -> dto.Post:
        ...

    async def delete_post(self, *, post_id: int) -> None:
        ...

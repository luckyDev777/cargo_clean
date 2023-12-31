from sqlalchemy import select

from src.business_logic.post import dto
from src.business_logic.post.exceptions import PostIdNotExists
from .base import SQLAlchemyDAO
from src.business_logic.post.interfaces.dao import PostDAO
from ..converters import convert_post_model_to_dto, convert_post_models_to_dtos
from ..exception_mapper import exception_mapper
from ..models import Post


class PostDAOImpl(SQLAlchemyDAO, PostDAO):

    @exception_mapper
    async def get_by_id(self, *, post_id: int) -> dto.Post:
        statement = select(Post).where(Post.id == post_id)
        post: Post | None = await self._session.scalar(statement=statement)

        if post:
            return convert_post_model_to_dto(post=post)

        raise PostIdNotExists(post_id=post_id)

    @exception_mapper
    async def create_post(self, *, post_name: str) -> dto.Post:
        new_post = Post(name=post_name)

        self._session.add(instance=new_post)

        await self._session.flush()

        return convert_post_model_to_dto(post=new_post)
    
    @exception_mapper
    async def get_posts(self) -> list[dto.Post]:
        statement = select(Post)
        posts: list[Post] = await self._session.scalars(statement=statement)
        return convert_post_models_to_dtos(posts)
    
    @exception_mapper
    async def update_post(self, *, post_id: int, post_info: dto.UpdatePost) -> dto.Post:
        statement = select(Post).where(Post.id == post_id)
        post: Post | None = await self._session.scalar(statement=statement)

        if post:
            post.name = post_info.name if post_info.name else post.name

            return convert_post_model_to_dto(post=post)

        raise PostIdNotExists(post_id=post_id)
    
    @exception_mapper
    async def delete_post(self, *, post_id: int) -> None:
        statement = select(Post).where(Post.id == post_id)
        post: Post | None = await self._session.scalar(statement=statement)

        if post:

            await self._session.delete(instance=post)
            return

        raise PostIdNotExists(post_id=post_id)

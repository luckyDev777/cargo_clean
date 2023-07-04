from src.business_logic.common.exceptions.dao import DAOError
from src.business_logic.common.interfaces.persistance.uow import UoW
from src.business_logic.post import dto
from src.business_logic.post.interfaces.dao import PostDAO


class CreatePostService:
    def __init__(self, dao: PostDAO, uow: UoW) -> None:
        self._dao = dao
        self._uow = uow

    async def __call__(self, post_info: dto.CreatePost) -> dto.Post:
        try:
            new_post = await self._dao.create_post(post_name=post_info.name)
        except DAOError as err:
            await self._uow.rollback()
            raise err

        await self._uow.commit()

        return new_post

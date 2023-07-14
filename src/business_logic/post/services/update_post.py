from src.business_logic.common.exceptions.dao import DAOError
from src.business_logic.common.interfaces.persistance.uow import UoW
from src.business_logic.post import dto
from src.business_logic.post.interfaces.dao import PostDAO


class UpdatePostService:
    def __init__(self, dao: PostDAO, uow: UoW) -> None:
        self._dao = dao
        self._uow = uow

    async def __call__(self, post_id: int, post_info: dto.CreatePost) -> dto.Post:
        try:
            updated_post = await self._dao.update_post(post_id=post_id, post_name=post_info.name)
        except DAOError as err:
            await self._uow.rollback()
            raise err

        await self._uow.commit()

        return updated_post
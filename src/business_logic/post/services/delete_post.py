from src.business_logic.common.exceptions.dao import DAOError
from src.business_logic.common.interfaces.persistance.uow import UoW
from src.business_logic.post import dto
from src.business_logic.post.interfaces.dao import PostDAO


class DeletePostService:
    def __init__(self, dao: PostDAO, uow: UoW) -> None:
        self._dao = dao
        self._uow = uow

    async def __call__(self, post_id: int) -> None:
        try:
            await self._dao.delete_post(post_id=post_id)
        except DAOError as err:
            await self._uow.rollback()
            raise err

        await self._uow.commit()

        return 
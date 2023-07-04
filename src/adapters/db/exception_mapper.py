from functools import wraps
from typing import Callable, Any

from sqlalchemy.exc import SQLAlchemyError

from src.business_logic.common.exceptions.dao import DAOError


def exception_mapper(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    async def wrapped(*args: Any, **kwargs: Any):
        try:
            return await func(*args, **kwargs)
        except SQLAlchemyError:
            raise DAOError

    return wrapped

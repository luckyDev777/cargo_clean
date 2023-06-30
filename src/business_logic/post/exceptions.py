from dataclasses import dataclass

from src.business_logic.common.exceptions.base import AppException


@dataclass
class PostIdNotExists(AppException):
    post_id: int

    @property
    def message(self) -> str:
        return f"Post with {self.post_id} does not exist"

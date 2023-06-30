from dataclasses import dataclass

from src.business_logic.common.dto.base import DTO


@dataclass(frozen=True)
class Post(DTO):
    post_id: int
    name: str


@dataclass(frozen=True)
class GetPost(DTO):
    post_id: int

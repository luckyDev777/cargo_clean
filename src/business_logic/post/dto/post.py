from dataclasses import dataclass
from typing import Optional

from src.business_logic.common.dto.base import DTO


@dataclass(frozen=True)
class Post(DTO):
    post_id: int
    name: str


@dataclass(frozen=True)
class GetPost(DTO):
    post_id: int


@dataclass(frozen=True)
class CreatePost(DTO):
    name: str


@dataclass(frozen=True)
class UpdatePost(DTO):
    name: str | None

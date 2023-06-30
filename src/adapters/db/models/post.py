from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class Post(BaseModel):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

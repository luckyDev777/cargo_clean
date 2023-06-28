from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel
from .user import User


class Post(BaseModel):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    content: Mapped[str]
    created_at: Mapped[DateTime] = mapped_column(default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(default=func.now())
    author_id = mapped_column(ForeignKey("users.id"))

    author: Mapped["User"] = relationship(back_populates="posts")

    def __repr__(self):
        return f"<Post(title='{self.title}', author_id='{self.author_id}')>"

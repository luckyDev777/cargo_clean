from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel
from .user import User


class Subscription(BaseModel):
    __tablename__ = "subscriptions"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id = mapped_column(ForeignKey("users.id"))
    author_id = mapped_column(ForeignKey("users.id"))

    users: Mapped[list["User"]] = relationship(back_populates="subscriptions")
    authors: Mapped[list["User"]] = relationship(back_populates="subscribers")

    def __repr__(self):
        return f"<Subscription(user_id='{self.user_id}', author_id='{self.author_id}')>"

import enum

from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel
from .donation import Donation
from .post import Post
from .subscription import Subscription


class Role(enum.Enum):
    AUTHOR = "author"
    READER = "reader"


class User(BaseModel):
    __tablename__ = "users"

    id: Mapped(int) = mapped_column(primary_key=True)
    name: Mapped(str) = mapped_column(String(30))
    email: Mapped(str) = mapped_column(String(100), unique=True)
    role: Mapped(enum) = mapped_column(Enum(Role), default=Role.READER)

    subscriptions: Mapped[list["Subscription"]] = relationship(back_populates="user")

    posts: Mapped[list["Post"]] = relationship(back_populates="author")

    donations: Mapped[list["Donation"]] = relationship(back_populates="donor")

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}', role='{self.role}')>"

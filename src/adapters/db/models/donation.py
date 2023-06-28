from decimal import Decimal

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel
from .user import User


class Donation(BaseModel):
    __tablename__ = "donations"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[Decimal]
    donor_id = mapped_column(ForeignKey("users.id"))
    author_id = mapped_column(ForeignKey("users.id"))

    donor: Mapped[list["User"]] = relationship(back_populates="donations")
    author: Mapped[list["User"]] = relationship(back_populates="received_donations")

    def __repr__(self):
        return f"<Donation(amount='{self.amount}', donor_id='{self.donor_id}', author_id='{self.author_id}')>"

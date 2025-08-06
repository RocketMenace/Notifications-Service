from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from .base import BaseModel


class User(BaseModel):
    first_name: Mapped[str] = mapped_column(String(length=100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(length=100), nullable=False)
    phone_number: Mapped[str] = mapped_column(
        String(length=12),
        unique=True,
        nullable=False,
    )
    email: Mapped[str] = mapped_column(
        String(length=100),
        unique=True,
        index=True,
        nullable=False,
    )
    telegram_link: Mapped[str] = mapped_column(
        String(length=100),
        unique=True,
        nullable=False,
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, email={self.email!r})"

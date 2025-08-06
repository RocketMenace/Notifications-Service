from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import BaseModel
from .notification import Notification


class User(BaseModel):
    __tablename__ = "users"

    first_name: Mapped[str] = mapped_column(String(length=100))
    last_name: Mapped[str] = mapped_column(
        String(length=100),
    )
    phone_number: Mapped[str] = mapped_column(
        String(length=12),
        unique=True,
    )
    email: Mapped[str] = mapped_column(
        String(length=100),
        unique=True,
        index=True,
    )
    telegram_link: Mapped[str] = mapped_column(
        String(length=100),
        unique=True,
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    notification: Mapped[list["Notification"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
        order_by="Notification.created_at.desc()",
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, email={self.email!r})"

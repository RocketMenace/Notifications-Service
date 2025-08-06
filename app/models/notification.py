from .base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, Boolean, String, Enum as SQLEnum
from .user import User
from enum import Enum


class NotificationStatus(Enum):
    FAILED = "Failed"
    COMPLETED = "Completed"
    PENDING = "Pending"


class NotificationType(Enum):
    TELEGRAM = "Telegram"
    EMAIL = "Email"
    SMS = "SMS"


class Notification(BaseModel):
    __tablename__ = "notifications"

    id: Mapped[int] = mapped_column(Integer, index=True, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="notifications")
    is_delivered: Mapped[bool] = mapped_column(Boolean, default=False)
    message: Mapped[str] = mapped_column(String(length=255))
    type: Mapped[NotificationType] = mapped_column(SQLEnum(NotificationType))
    status: Mapped[NotificationStatus] = mapped_column(
        SQLEnum(NotificationStatus),
        default=NotificationStatus.PENDING,
    )

from .base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, ForeignKey, Boolean, String, Enum as SQLEnum
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
    is_delivered: Mapped[bool] = mapped_column(Boolean, default=False)
    message: Mapped[str] = mapped_column(String(length=255))
    type: Mapped[NotificationType] = mapped_column(SQLEnum(NotificationType))
    status: Mapped[NotificationStatus] = mapped_column(
        SQLEnum(NotificationStatus),
        default=NotificationStatus.PENDING,
    )

    def __repr__(self):
        return (
            f"Notification(id={self.id!r}, type={self.email!r}), status={self.status!r}"
        )

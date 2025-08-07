from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseRepository
from app.models.notification import Notification


class NotificationRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session=session, model=Notification)

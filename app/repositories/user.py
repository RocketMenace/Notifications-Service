from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseRepository
from app.models.user import User


class UserRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session=session, model=User)

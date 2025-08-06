from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from app.config.settings import settings


class Database:
    def __init__(self):
        self.engine = create_async_engine(settings.db_url, echo=True, future=True)
        self.Base = declarative_base()

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async_session = async_sessionmaker(self.engine, class_=AsyncSession)
        session = None
        try:
            session = async_session()
            async with session:
                yield session
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()


database = Database()

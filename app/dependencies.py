from dishka import Scope, provide, Provider
from sqlalchemy.ext.asyncio import AsyncSession
from app.config.db import database
from app.repositories.user import UserRepository
from app.services.user import UserService


class DatabaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def get_db_session(self) -> None:
        await database.get_session()


class UserRepositoryProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def get_user_repository(self, session: AsyncSession) -> UserRepository:
        return UserRepository(session=session)


class UserServiceProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def get_user_service(self, repository: UserRepository) -> UserService:
        return UserService(repository=repository)

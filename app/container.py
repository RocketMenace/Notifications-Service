from dishka import make_async_container
from app.dependencies import (
    DatabaseProvider,
    UserRepositoryProvider,
    UserServiceProvider,
)

container = make_async_container(
    DatabaseProvider(),
    UserRepositoryProvider(),
    UserServiceProvider(),
)

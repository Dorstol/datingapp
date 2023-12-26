from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from src.core.models import User
from src.users.config import auth_backend
from src.users.manager import get_user_manager
from src.users.schemas import UserRead, UserCreate

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app = FastAPI(title="Dating-app")

app.include_router(
    fastapi_users.get_auth_router(backend=auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

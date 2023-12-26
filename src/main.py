from fastapi import FastAPI

from src.users.config import auth_backend, fastapi_users
from src.users.schemas import UserRead, UserCreate

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


current_user = fastapi_users.current_user()

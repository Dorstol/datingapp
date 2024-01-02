from fastapi import FastAPI

from src.users.config import auth_backend, fastapi_users
from src.users.schemas import UserRead, UserCreate
from src.matches.router import router as match_router


app = FastAPI(title="Dating-app")

app.include_router(
    fastapi_users.get_auth_router(backend=auth_backend),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    match_router,
    prefix="/matches",
    tags=["Matches"],
)


current_user = fastapi_users.current_user()

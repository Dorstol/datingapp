import os
from typing import Optional

from dotenv import load_dotenv
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin
from starlette.responses import Response

from src.database import get_user_db
from src.users.models import User

load_dotenv()

SECRET = os.getenv("SECRET")


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(
        self, user: User, request: Optional[Request] = None
    ) -> Response:
        return Response(
            "You are successfully register!",
        )

    async def on_after_login(
        self,
        user: User,
        request: Optional[Request] = None,
        response: Optional[Response] = None,
    ) -> Response:
        return Response(
            "You are successfully authorized!",
        )


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)

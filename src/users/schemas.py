from typing import Optional

from fastapi_users import schemas
from pydantic import EmailStr

from src.users.models import UserGender, GenderInterests


class UserRead(schemas.BaseUser[int]):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    gender: UserGender
    interests: GenderInterests
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        from_attributes = True


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    last_name: str
    email: EmailStr
    gender: UserGender
    interests: GenderInterests
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    pass

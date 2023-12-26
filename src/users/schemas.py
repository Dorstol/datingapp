from typing import Optional, List

from fastapi_users import schemas
from pydantic import EmailStr

from src.core.models.users import GenderEnum


class UserRead(schemas.BaseUser[int]):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    gender: GenderEnum
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    last_name: str
    email: EmailStr
    gender: GenderEnum
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    pass

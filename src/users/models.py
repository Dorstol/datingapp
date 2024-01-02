import enum

from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import Enum, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from src.base import Base


class UserGender(str, enum.Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class GenderInterests(str, enum.Enum):
    MALE = "male"
    FEMALE = "female"
    EVERYONE = "everyone"


class User(SQLAlchemyBaseUserTable[int], Base):
    """
    User model
    """

    __tablename__ = "user"

    first_name: Mapped[str] = mapped_column(String(32), nullable=True)
    last_name: Mapped[str] = mapped_column(String(32), nullable=True)
    gender: Mapped[str] = mapped_column(Enum(UserGender))
    interests: Mapped[str] = mapped_column(Enum(GenderInterests))
    email: Mapped[str] = mapped_column(
        String(length=320), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

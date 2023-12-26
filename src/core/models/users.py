from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import Enum, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from src.core.models.base import Base


class GenderEnum(str, Enum):
    male = "male"
    female = "female"


class User(SQLAlchemyBaseUserTable[int], Base):
    first_name: Mapped[str] = mapped_column(String(32))
    last_name: Mapped[str] = mapped_column(String(32))
    email: Mapped[str] = mapped_column(
        String(length=320), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

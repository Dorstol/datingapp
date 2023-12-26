import enum
from datetime import datetime
from sqlalchemy import func
from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import Enum, String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.models.base import Base


class GenderEnum(enum.Enum):
    male = "male"
    female = "female"
    alien = "alien"


class User(SQLAlchemyBaseUserTable[int], Base):
    first_name: Mapped[str] = mapped_column(String(32), nullable=True)
    last_name: Mapped[str] = mapped_column(String(32), nullable=True)
    gender: Mapped[str] = mapped_column(Enum(GenderEnum), default=GenderEnum.alien)
    email: Mapped[str] = mapped_column(
        String(length=320), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    matches: Mapped["Match"] = relationship(back_populates="matches")


class Match(Base):
    user_id_1: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user_id_2: Mapped[int] = mapped_column(ForeignKey("user.id"))
    matched_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.utcnow,
    )
    is_accepted: Mapped[bool] = mapped_column(Boolean, default=False)

    user_1: Mapped[User] = relationship(back_populates="from_user")
    user_2: Mapped[User] = relationship(back_populates="to_user")

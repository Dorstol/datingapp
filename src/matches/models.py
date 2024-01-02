import sqlalchemy.sql
from sqlalchemy import Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.users.models import User
from src.base import Base


class Match(Base):
    """
    Match model
    """

    __tablename__ = "match"

    user_id_1: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=True, default=User.id)
    user_id_2: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=True, server_default="")
    is_accepted: Mapped[bool] = mapped_column(Boolean, server_default=sqlalchemy.sql.false())
    user_1 = relationship(User, foreign_keys=[user_id_1])
    user_2 = relationship(User, foreign_keys=[user_id_2])

from datetime import datetime

from sqlalchemy import Boolean, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.base import Base, users_matches


class Match(Base):
    """
    Match model
    """

    __tablename__ = "match"

    is_accepted: Mapped[bool] = mapped_column(Boolean, default=False)
    created: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.utcnow,
    )
    users = relationship(
        "User",
        secondary=users_matches,
        back_populates="matches",
    )

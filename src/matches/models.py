import json
from typing import List, Optional

from sqlalchemy import ForeignKey, Integer, ARRAY
from src.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.users.models import User


class Match(Base):
    """
    Match model
    """

    __tablename__ = "match"

    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("user.id"),
        primary_key=True,
    )
    users_list: Mapped[Optional[List]] = mapped_column(ARRAY(Integer))
    user_1 = relationship(User, foreign_keys=[user_id])

    def set_my_list(self, my_list: list):
        self.users_list = json.dumps(my_list)

    def get_my_list(self):
        return json.loads(self.users_list) if self.users_list else []

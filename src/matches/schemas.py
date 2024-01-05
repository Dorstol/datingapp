from typing import Annotated, List

from annotated_types import Ge
from pydantic import BaseModel


class Match(BaseModel):
    user_id: Annotated[int, Ge(1)]
    users_list: List[int]


class MatchCreate(Match):
    pass

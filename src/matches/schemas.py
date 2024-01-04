from pydantic import BaseModel
from typing import Annotated, List
from annotated_types import Ge


class MatchModel(BaseModel):
    user_id_1: Annotated[int, Ge(1)]
    users_list: List[int]

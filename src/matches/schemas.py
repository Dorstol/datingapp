from pydantic import BaseModel
from typing import Annotated
from annotated_types import Ge


class MatchModel(BaseModel):
    user_id_1: Annotated[int, Ge(1)]
    user_id_2: Annotated[int, Ge(1)]
    is_accepted: bool

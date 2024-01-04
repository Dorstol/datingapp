from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.matches.models import Match


async def _create_match(
    user_id_1: int,
    user_id_2: int,
    session: AsyncSession = Depends(get_async_session),
):
    pass

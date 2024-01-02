from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.users.models import User
from .crud import _create_match

router = APIRouter()


@router.post("/create_match/{user_id_1}/{user_id_2}/")
async def create_match_api(
        user_id_1: int,
        user_id_2: int,
        session: AsyncSession = Depends(get_async_session),
):
    user_1_result = await session.execute(select(User).filter(User.id == user_id_1))
    user_2_result = await session.execute(select(User).filter(User.id == user_id_2))

    user_1 = user_1_result.fetchone()
    user_2 = user_2_result.fetchone()

    if not user_1 or not user_2:
        raise HTTPException(status_code=404, detail="Users not found")

    # Await the result of _create_match
    match = await _create_match(user_id_1, user_id_2, session)

    return match

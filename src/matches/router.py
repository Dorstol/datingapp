from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.users.models import User
from .crud import _create_match

router = APIRouter()


@router.post("/create_match/{user_id_1}/{user_id_2}/")
async def create_match_api(
    session: AsyncSession = Depends(get_async_session),
):
    pass

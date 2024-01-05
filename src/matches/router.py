from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import session_dependency
from src.matches.crud import _get_matches, _get_match, _create_match
from src.matches.schemas import Match, MatchCreate

router = APIRouter()


@router.get("/")
async def get_matches(
    session: AsyncSession = Depends(session_dependency),
) -> list[Match]:
    return await _get_matches(session)


@router.get("/{match_id/}")
async def get_match(match_id: int, session: AsyncSession = Depends(session_dependency)):
    return await _get_match(match_id, session)


@router.post("/create_match/")
async def create_match_api(
    match_in: MatchCreate, session: AsyncSession = Depends(session_dependency)
):
    return await _create_match(match_in, session)

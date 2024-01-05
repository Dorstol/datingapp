from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from src.matches.models import Match as MatchModel
from src.matches.schemas import Match, MatchCreate


async def _get_matches(session: AsyncSession) -> list[Match]:
    query = select(MatchModel)
    result: Result = await session.execute(query)
    matches = result.scalars().all()
    return list(matches)


async def _get_match(match_id: int, session: AsyncSession) -> Match | None:
    return await session.get(MatchModel, match_id)


async def _create_match(
    match_in: MatchCreate,
    session: AsyncSession,
) -> Match:
    match = MatchModel(**match_in.model_dump())
    session.add(match)
    await session.commit()
    return match

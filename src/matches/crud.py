from sqlalchemy import select, Result, text
from sqlalchemy.ext.asyncio import AsyncSession

from src.matches.models import Match as MatchModel
from src.matches.schemas import Match, CreateOrUpdateMatch
from fastapi.responses import UJSONResponse


async def _get_matches(session: AsyncSession) -> list[Match]:
    query = select(MatchModel)
    result: Result = await session.execute(query)
    matches = result.scalars().all()
    return list(matches)


async def _get_match(match_id: int, session: AsyncSession) -> Match | None:
    return await session.get(MatchModel, match_id)


async def _create_or_update_match(
    match_in: CreateOrUpdateMatch,
    session: AsyncSession,
) -> Match | UJSONResponse:
    match = await session.get(MatchModel, match_in.user_id)
    if match:
        query = f"UPDATE match SET users_list=array_append(users_list, '{int(''.join(str(digit) for digit in match_in.users_list))}') WHERE user_id = {match_in.user_id}"
        await session.execute(text(query))
        await session.commit()
        return UJSONResponse(
            {
                "status": 200,
            }
        )
    else:
        match = MatchModel(**match_in.model_dump())
        session.add(match)
        await session.commit()
        return match

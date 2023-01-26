from fastapi import APIRouter, Depends, status
from sqlmodel import select

from app.db import get_session, AsyncSession
from app.models.position import Position

router = APIRouter(prefix="/positions", tags=["Positions"])


@router.post("/", response_model=Position)
async def create_position(*, new_position: Position, session: AsyncSession = Depends(get_session)) -> Position:
    return await session.add(new_position)


@router.get("/", response_model=list[Position])
async def list_positions(*, session: AsyncSession = Depends(get_session)) -> list[Position]:
    return await session.exec(select(Position))


@router.get("/{position_id}", response_model=Position)
async def get_search(*, position_id: int, session: AsyncSession = Depends(get_session)) -> Position:
    return await session.exec(select(Position).where(Position.id == position_id)).one()


@router.delete("/{position_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_search(*, position_id: int, session: AsyncSession = Depends(get_session)):
    to_del = get_search(position_id=position_id)
    await session.delete(to_del)

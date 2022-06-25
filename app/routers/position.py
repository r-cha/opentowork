from fastapi import APIRouter, status

from app.db import positions
from app.models.position import Position, PositionCreate

router = APIRouter(prefix="/positions", tags=["Positions"])


@router.post("/", response_model=Position)
async def create_position(new_position: PositionCreate) -> Position:
    return await positions.create(new_position)


@router.get("/", response_model=list[Position])
async def list_positions() -> list[Position]:
    return await positions.list()


@router.get("/{position_id}", response_model=Position)
async def get_search(position_id: int) -> Position:
    return await positions.get(position_id)


@router.delete("/{position_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_search(position_id: int):
    await positions.delete(position_id)

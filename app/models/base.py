from datetime import datetime
from sqlmodel import SQLModel, Field


class DBModel(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    created_on: datetime | None
    updated_on: datetime | None

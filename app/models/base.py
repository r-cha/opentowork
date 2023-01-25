from datetime import datetime
from sqlmodel import SQLModel


class DBModel(SQLModel):
    id: int | None
    created_on: datetime | None
    updated_on: datetime | None

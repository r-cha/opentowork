from datetime import datetime
from pydantic import BaseModel


class DBModel(BaseModel):
    id: int | None
    created_on: datetime | None
    updated_on: datetime | None

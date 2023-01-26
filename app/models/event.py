from datetime import datetime
from enum import Enum

from sqlmodel import Field

from app.models.base import DBModel
from app.models.position import Position


class EventKind(str, Enum):
    EMAIL = "EMAIL"
    SCREENING = "SCREENING"
    TECHNICAL_INTERVIEW = "TECHNICAL_INTERVIEW"
    ASSESSMENT = "ASSESSMENT"
    CULTURE = "CULTURE"
    EXECUTIVE = "EXECUTIVE"


class InterviewEvent(DBModel):
    kind: EventKind
    position: Position
    date: datetime
    contact: str = Field(..., description="phone number, zoom link, etc")

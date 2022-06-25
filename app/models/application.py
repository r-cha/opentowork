from datetime import datetime
from enum import Enum

from app.models.base import DBModel
from app.models.position import Position
from app.models.event import InterviewEvent


class ApplicationStatus(str, Enum):
    SUBMITTED = "SUBMITTED"
    UNDER_REVIEW = "UNDER_REVIEW"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    # and more


class ApplicationMaterials(DBModel):
    # TODO: Each document will be in S3
    resume: str  # or file
    cover_letter: str  # or file
    notes: str


class ApplicationProcess(DBModel):
    position: Position
    status: ApplicationStatus
    updated_on: datetime
    events: list[InterviewEvent]
    materials: ApplicationMaterials

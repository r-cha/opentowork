from pydantic import BaseModel


class User(BaseModel):
    """Only the basic metadata of a user"""

    name: str
    email: str
    # etc...


class Applicant(User):
    """Details of the user as a persona"""

    resume: str  # actually a document somewhere
    industry: str  # probably another table or enum
    # etc...

from pydantic import BaseModel, Field


class MessageSchema(BaseModel):
    text: str
    bio: str


class ClassifiedMessageSchema(BaseModel):
    lead: bool


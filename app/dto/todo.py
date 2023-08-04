from uuid import UUID
from datetime import datetime

from pydantic import BaseModel


class TodoResponse(BaseModel):
    id: UUID
    title: str
    description: str
    created_at: datetime

    class Config:
        orm_mode = True


class TodoModifyRequest(BaseModel):
    title: str
    description: str

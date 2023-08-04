from datetime import datetime
from uuid import UUID, uuid4

from beanie import Document
from pydantic import Field


class Todo(Document):
    id: UUID = Field(default_factory=uuid4)
    title: str
    description: str
    created_at: datetime

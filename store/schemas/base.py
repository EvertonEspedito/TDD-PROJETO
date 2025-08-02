from datetime import datetime, timezone

from uuid import UUID
import uuid

from pydantic import BaseModel, Field


class BaseSchemaMixin(BaseModel):
    id: UUID = Field(default_factory = uuid.uuid4)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    update_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

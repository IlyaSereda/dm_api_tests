from typing import Optional
from pydantic import BaseModel, Extra, Field
from __future__ import annotations


class UserDetailsEnvelope(BaseModel):
    class Config:
        extra = Extra.forbid

    resource: Optional[UserDetails] = None
    metadata: Optional[Any] = Field(None, description='Additional metadata')

from typing import Any, Optional
from pydantic import BaseModel, Extra, Field


class UserDetailsEnvelope(BaseModel):
    class Config:
        extra = Extra.forbid

    #resource: Optional[UserDetails] = None
    #metadata: Optional[Any] = Field(None, description='Additional metadata')

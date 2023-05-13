from typing import Optional
from pydantic import BaseModel, StrictStr, Field, Extra
from __future__ import annotations

class ResetPassword(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = Field(None, description='Login')
    email: Optional[StrictStr] = Field(None, description='Email')
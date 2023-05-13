from typing import Optional
from pydantic import BaseModel, StrictStr, Field, Extra
from __future__ import annotations

class LoginCredentials(BaseModel):
    class Config:
        extra = Extra.forbid

        login: Optional[StrictStr] = None
        email: Optional[StrictStr] = None
        remember_me: Optional[bool] = Field(None, alias='rememberMe')

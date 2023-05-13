from typing import Optional
from pydantic import BaseModel, StrictStr, Extra, Field
from __future__ import annotations


class GeneralError(BaseModel):
    class Config:
        extra = Extra.forbid

    message: Optional[StrictStr] = Field(None, description='Client message')

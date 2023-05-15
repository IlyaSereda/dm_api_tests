from typing import List, Optional, Dict
from pydantic import BaseModel, StrictStr, Extra, Field


class BadRequestError(BaseModel):
    class Config:
        extra = Extra.forbid

    message: Optional[StrictStr] = Field(None, description='Client message')
    invalid_properties: Optional[Dict[str, List[StrictStr]]] = Field(
        None,
        alias='invalidProperties',
        description='Key-value pairs of invalid request properties',
    )

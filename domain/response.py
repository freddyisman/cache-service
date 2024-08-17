from pydantic import BaseModel
from typing import Dict, Any


class AddPayloadResponse(BaseModel):
    data: Dict[str, Any]
    status: int
    message: str


class GetPayloadResponse(BaseModel):
    data: Dict[str, Any]
    status: int
    message: str

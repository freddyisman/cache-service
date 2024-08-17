from pydantic import BaseModel
from typing import List


class PayloadRequest(BaseModel):
    list_1: List[str]
    list_2: List[str]

from pydantic import BaseModel
from typing import List


class Payload(BaseModel):
    from_msg : str
    to_msg: List[str]
    subject: str
    body: str
from pydantic import BaseModel
from simplestr import gen_str_repr


@gen_str_repr
class Ping(BaseModel):
    id: str
    success: bool
    timestamp: int
    timestamp_str: str

    def __init__(self, id: str, success: bool, timestamp: int, timestamp_str: str) -> None:
        super().__init__(id=id, success=success, timestamp=timestamp, timestamp_str=timestamp_str)

from pydantic import BaseModel
from simplestr import gen_str_repr


@gen_str_repr
class Book(BaseModel):
    id: str
    title: str
    author_id: str
    publish_year: int
    description: str
    created_timestamp: int
    updated_timestamp: int

    def __init__(self, id: str, title: str, author_id: str, publish_year: int, description: str, created_timestamp: int, updated_timestamp: int) -> None:
        super().__init__(id=id, title=title, author_id=author_id, publish_year=publish_year, description=description, created_timestamp=created_timestamp, updated_timestamp=updated_timestamp)

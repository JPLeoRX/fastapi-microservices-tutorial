from pydantic import BaseModel
from simplestr import gen_str_repr


@gen_str_repr
class BookUpdate(BaseModel):
    id: str
    title: str
    author_id: str
    publish_year: int
    description: str

    def __init__(self, id: str, title: str, author_id: str, publish_year: int, description: str) -> None:
        super().__init__(id=id, title=title, author_id=author_id, publish_year=publish_year, description=description)

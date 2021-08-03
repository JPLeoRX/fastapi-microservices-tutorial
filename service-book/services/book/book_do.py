from sqlalchemy import Column, String, Integer, BigInteger
from database import Base
from simplestr import gen_str_repr


@gen_str_repr
class BookDO(Base):
    __tablename__ = 'book'

    id = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    author_id = Column(String, index=True)
    publish_year = Column(Integer, index=True)
    description = Column(String)
    created_timestamp = Column(BigInteger)
    updated_timestamp = Column(BigInteger)

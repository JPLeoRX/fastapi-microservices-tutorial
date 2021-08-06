from typing import List
from sqlalchemy.orm import Session


class AbstractServiceDatabase:
    def get_all(self, db: Session, offset: int = 0, limit: int = 100) -> List:
        pass

    def get_by_id(self, db: Session, id: str):
        pass

    def add(self, db: Session, item_add):
        pass

    def update(self, db: Session, item_update):
        pass

    def delete(self, db: Session, id: str):
        pass

from typing import List
from sqlalchemy.orm import Session
from library_message_protocol import Book, BookAdd, BookUpdate
from library_utils import AbstractServiceDatabase
from services.book.book_do import BookDO
from services.book.converter_book import ConverterBook
from injectable import injectable, autowired, Autowired


@injectable
class ServiceBook(AbstractServiceDatabase):
    @autowired
    def __init__(self, converter: Autowired(ConverterBook)):
        self.converter = converter

    def get_all(self, db: Session, offset: int = 0, limit: int = 100) -> List[Book]:
        items_do = db.query(BookDO).order_by(BookDO.title).offset(offset).limit(limit).all()
        return self.converter.map_list_do_to_list_mo(items_do)

    def get_by_id(self, db: Session, id: str) -> Book:
        item_do = db.query(BookDO).filter(BookDO.id == id).first()
        return self.converter.map_do_to_mo(item_do)

    def add(self, db: Session, item_add: BookAdd) -> Book:
        item_mo = self.converter.map_add_to_mo(item_add)
        item_do = self.converter.map_mo_to_do(item_mo)
        db.add(item_do)
        db.commit()
        return item_mo

    def update(self, db: Session, item_update: BookUpdate) -> Book:
        item_mo = self.get_by_id(db, item_update.id)
        item_mo = self.converter.map_update_to_mo(item_mo, item_update)
        item_do = self.converter.map_mo_to_do(item_mo)
        db.merge(item_do)
        db.commit()
        return item_mo

    def delete(self, db: Session, id: str) -> Book:
        item_mo = self.get_by_id(db, id)
        db.query(BookDO).filter(BookDO.id == id).delete()
        db.commit()
        return item_mo

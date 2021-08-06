from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from library_message_protocol import Book, BookAdd, BookUpdate
from services.book.service_book import ServiceBook


router_book = APIRouter()
service_book = ServiceBook()


@router_book.get("/book/get_all", response_model=List[Book])
def get_all(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> List[Book]:
    return service_book.get_all(db, offset, limit)


@router_book.get("/book/get_by_id", response_model=Book)
def get_by_id(id: str, db: Session = Depends(get_db)) -> Book:
    return service_book.get_by_id(db, id)


@router_book.post("/book/add", response_model=Book)
def add(item_add: BookAdd, db: Session = Depends(get_db)) -> Book:
    return service_book.add(db, item_add)


@router_book.put("/book/update", response_model=Book)
def update(item_update: BookUpdate, db: Session = Depends(get_db)) -> Book:
    return service_book.update(db, item_update)


@router_book.delete("/book/delete", response_model=Book)
def delete(id: str, db: Session = Depends(get_db)) -> Book:
    return service_book.delete(db, id)

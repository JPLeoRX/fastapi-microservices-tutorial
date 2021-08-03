from .book_do import BookDO
from library_message_protocol import Book, BookAdd, BookUpdate
from library_utils import AbstractConverter
from injectable import injectable, autowired, Autowired


@injectable
class ConverterBook(AbstractConverter):
    @autowired
    def __init__(self):
        pass

    def map_do_to_mo(self, item_do: BookDO) -> Book:
        pass

    def map_mo_to_do(self, item_mo: Book) -> BookDO:
        pass

    def map_add_to_mo(self, item_add: BookAdd) -> Book:
        pass

    def map_update_to_mo(self, item_update: BookUpdate) -> Book:
        pass

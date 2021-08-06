from .book_do import BookDO
from library_message_protocol import Book, BookAdd, BookUpdate
from library_utils import AbstractConverter, UtilsId, UtilsTime
from injectable import injectable, autowired, Autowired


@injectable
class ConverterBook(AbstractConverter):
    @autowired
    def __init__(self, utils_id: Autowired(UtilsId), utils_time: Autowired(UtilsTime)):
        self.utils_id = utils_id
        self.utils_time = utils_time

    def map_do_to_mo(self, item_do: BookDO) -> Book:
        return Book(
            id=item_do.id,
            title=item_do.title,
            author_id=item_do.author_id,
            publish_year=item_do.publish_year,
            description=item_do.description,
            created_timestamp=item_do.created_timestamp,
            updated_timestamp=item_do.updated_timestamp
        )

    def map_mo_to_do(self, item_mo: Book) -> BookDO:
        return BookDO(
            id=item_mo.id,
            title=item_mo.title,
            author_id=item_mo.author_id,
            publish_year=item_mo.publish_year,
            description=item_mo.description,
            created_timestamp=item_mo.created_timestamp,
            updated_timestamp=item_mo.updated_timestamp
        )

    def map_add_to_mo(self, item_add: BookAdd) -> Book:
        return Book(
            id=self.utils_id.generate_uuid(),
            title=item_add.title,
            author_id=item_add.author_id,
            publish_year=item_add.publish_year,
            description=item_add.description,
            created_timestamp=self.utils_time.get_current_timestamp_ms(),
            updated_timestamp=self.utils_time.get_current_timestamp_ms()
        )

    def map_update_to_mo(self, item_old: Book, item_update: BookUpdate) -> Book:
        return Book(
            id=item_old.id,
            title=item_update.title,
            author_id=item_update.author_id,
            publish_year=item_update.publish_year,
            description=item_update.description,
            created_timestamp=item_old.created_timestamp,
            updated_timestamp=self.utils_time.get_current_timestamp_ms()
        )

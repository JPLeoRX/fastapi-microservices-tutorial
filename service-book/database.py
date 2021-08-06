from yoyo import read_migrations
from yoyo import get_backend
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "postgresql://library_user:qwe123@postgres/library_book_database"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def migration():
    print('Started SQL migrations')
    backend = get_backend(DATABASE_URL)
    migrations = read_migrations('database_migrations')
    with backend.lock():
        backend.apply_migrations(backend.to_apply(migrations))
    print('Finished SQL migrations')

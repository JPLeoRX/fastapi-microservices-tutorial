CREATE USER library_user WITH PASSWORD 'qwe123';
CREATE DATABASE library_book_database;
GRANT ALL PRIVILEGES ON DATABASE library_book_database TO library_user;
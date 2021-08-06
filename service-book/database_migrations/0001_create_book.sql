CREATE TABLE book
(
    id VARCHAR(256) NOT NULL,
    title VARCHAR(256) NOT NULL,
    author_id VARCHAR(256) NOT NULL,
    publish_year INTEGER NOT NULL,
    description VARCHAR(1024) NOT NULL,
    created_timestamp BIGINT NOT NULL,
    updated_timestamp BIGINT NOT NULL,
    PRIMARY KEY (id)
);
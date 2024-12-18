CREATE TABLE IF NOT EXISTS titles (
    title VARCHAR(255) PRIMARY KEY,
    is_book BOOLEAN NOT NULL,
    vector BLOB NOT NULL
);

CREATE TABLE IF NOT EXISTS contents (
    content TEXT, -- Or use VARCHAR()
    title VARCHAR(255) REFERENCES titles (title) ON DELETE CASCADE,
    vector BLOB NOT NULL,
    PRIMARY KEY (title, content)
);

CREATE TABLE IF NOT EXISTS list (
    title VARCHAR(255) PRIMARY KEY,
    done BOOLEAN DEFAULT FALSE,
    is_book BOOLEAN NOT NULL,
)
-- Create an index on title to optimize queries filtering by it
CREATE INDEX IF NOT EXISTS idx_contents_title ON contents (title);

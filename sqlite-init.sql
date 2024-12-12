CREATE TABLE IF NOT EXISTS titles (
    title VARCHAR(255) PRIMARY KEY,
    is_book BOOLEAN NOT NULL,
    vector BLOB NOT NULL
);

CREATE TABLE contents (
    content TEXT, -- Or use VARCHAR()
    title VARCHAR(255) REFERENCES titles (title) ON DELETE CASCADE,
    vector VECTOR (1024), -- Ensure this matches the embedding dims
    PRIMARY KEY (title, content)
);

-- Create an index on title to optimize queries filtering by it
CREATE INDEX idx_contents_title ON contents (title);

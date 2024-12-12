import sqlite3
import pickle  # Using pickle for serialization

# Set up the SQLite database
db = sqlite3.connect("sqlite.db")

# Create a table to store embeddings
db.execute("""
CREATE TABLE embeddings (
    id INTEGER PRIMARY KEY,
    vector BLOB
)
""")

# Example vector
embedding = [0.1, 0.2, 0.3, 0.4]

# Serialize the vector using pickle
serialized_vector = pickle.dumps(embedding)

# Insert serialized vector into the table
db.execute("INSERT INTO embeddings (vector) VALUES (?)", [serialized_vector])
db.commit()

# Retrieve the serialized vector from the database
result = db.execute("SELECT vector FROM embeddings WHERE id = 1").fetchone()
stored_vector = pickle.loads(result[0])

# Print the deserialized vector
print("Stored vector:", stored_vector)

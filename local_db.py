import sqlite3
import pickle  # Using pickle for serialization

# Set up the SQLite database
local_db = sqlite3.connect("sqlite.db")

# Read the SQL file
with open('sqlite_init.sql', 'r', encoding='utf-8') as file:
    sqlite_init = file.read()

# Split the SQL script by semicolon (;) to separate individual statements
sql_statements = sqlite_init.split(';')

# Execute each statement individually
for statement in sql_statements:
    statement = statement.strip()  # Remove extra whitespace
    if statement:  # Only execute non-empty statements
        local_db.execute(statement)

embedding = [0.1, 0.2, 0.3, 0.4]

# Serialize the vector using pickle
serialized_vector = pickle.dumps(embedding)

# Commit changes and close the connection
# db.commit()
# db.close()

import sqlite3
from config import Config

conn = sqlite3.connect(Config.DATABASE_PATH)

# Create a cursor object
cur = conn.cursor()

cur.execute("""
CREATE TABLE login (
    email TEXT PRIMARY KEY,
    name TEXT,
    hash TEXT
)
""")

cur.execute("""
CREATE TABLE users (
    email TEXT PRIMARY KEY,
    entries INTEGER DEFAULT 0
)
""")

# Commit the transaction
conn.commit()

conn.close()
print('Tables created successfully')
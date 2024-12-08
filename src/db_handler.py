import sqlite3

def init_db(db_path='database/example.db', schema_path='database/schema.sql'):
    conn = sqlite3.connect(db_path)
    with open(schema_path, 'r') as schema:
        conn.executescript(schema.read())
    conn.close()

def get_connection(db_path='database/example.db'):
    return sqlite3.connect(db_path)
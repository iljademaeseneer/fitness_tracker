import sqlite3

def init_db(db_path='database/example.db', schema_path='database/schema.sql'):
    conn = sqlite3.connect(db_path)
    with open(schema_path, 'r') as schema:
        conn.executescript(schema.read())
    conn.close()

def get_connection(db_path='database/example.db'):
    return sqlite3.connect(db_path)

def add_exercise(name, sets, reps, db_path='database/example.db'):
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO exercises (name, sets, reps) VALUES (?, ?, ?)", (name, sets, reps))
    conn.commit()
    conn.close()

def list_exercises(db_path='database/example.db'):
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, sets, reps, date FROM exercises")
    rows = cursor.fetchall()
    conn.close()
    return rows

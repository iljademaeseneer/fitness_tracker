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

def delete_exercise(exercise_id, db_path='database/example.db'):
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM exercises WHERE id = ?", (exercise_id,))
    conn.commit()
    conn.close()

def update_exercise(exercise_id, name=None, sets=None, reps=None, db_path='database/example.db'):
    conn = get_connection(db_path)
    cursor = conn.cursor()
    if name:
        cursor.execute("UPDATE exercises SET name = ? WHERE id = ?", (name, exercise_id))
    if sets:
        cursor.execute("UPDATE exercises SET sets = ? WHERE id = ?", (sets, exercise_id))
    if reps:
        cursor.execute("UPDATE exercises SET reps = ? WHERE id = ?", (reps, exercise_id))
    conn.commit()
    conn.close()

def filter_exercises_by_date(date, db_path='database/example.db'):
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, sets, reps, date FROM exercises WHERE date = ?", (date,))
    rows = cursor.fetchall()
    conn.close()
    return rows



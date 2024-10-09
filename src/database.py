import sqlite3

DATABASE = 'scores.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    with open('schema.sql', mode='r') as f:
        conn.cursor().executescript(f.read())
    conn.commit()
    conn.close()

def save_score(attempts):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('INSERT INTO scores (attempts) VALUES (?)', (attempts,))
    conn.commit()
    conn.close()

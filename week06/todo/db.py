import sqlite3

DATABASE = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS todos (\n            id INTEGER PRIMARY KEY AUTOINCREMENT,\n            title TEXT NOT NULL,\n            is_completed INTEGER NOT NULL DEFAULT 0,\n            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n        )
    ''')
    conn.commit()
    conn.close()

def get_todos():
    conn = get_db_connection()
    todos = conn.execute('SELECT * FROM todos ORDER BY created_at ASC').fetchall()
    conn.close()
    return todos

def add_todo(title):
    conn = get_db_connection()
    conn.execute('INSERT INTO todos (title) VALUES (?)', (title,))
    conn.commit()
    conn.close()

def toggle_todo(todo_id):
    conn = get_db_connection()
    todo = conn.execute('SELECT is_completed FROM todos WHERE id = ?', (todo_id,)).fetchone()
    if todo:
        new_status = 1 if todo['is_completed'] == 0 else 0
        conn.execute('UPDATE todos SET is_completed = ? WHERE id = ?', (new_status, todo_id))
        conn.commit()
    conn.close()

def delete_todo(todo_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
    conn.commit()
    conn.close()

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            is_completed INTEGER NOT NULL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = get_db_connection()
    todos = conn.execute('SELECT * FROM todos ORDER BY created_at ASC').fetchall()
    conn.close()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    if title:
        conn = get_db_connection()
        conn.execute('INSERT INTO todos (title) VALUES (?)', (title,))
        conn.commit()
        conn.close()
    return redirect(url_for('index'))

@app.route('/toggle/<int:todo_id>', methods=['POST'])
def toggle(todo_id):
    conn = get_db_connection()
    todo = conn.execute('SELECT is_completed FROM todos WHERE id = ?', (todo_id,)).fetchone()
    if todo:
        new_status = 1 if todo['is_completed'] == 0 else 0
        conn.execute('UPDATE todos SET is_completed = ? WHERE id = ?', (new_status, todo_id))
        conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

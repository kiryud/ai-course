from flask import Flask, render_template, request, redirect, url_for
import db

app = Flask(__name__)
DATABASE = db.DATABASE
init_db = db.init_db

@app.route('/')
def index():
    todos = db.get_todos()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    if title:
        db.add_todo(title)
    return redirect(url_for('index'))

@app.route('/toggle/<int:todo_id>', methods=['POST'])
def toggle(todo_id):
    db.toggle_todo(todo_id)
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete(todo_id):
    db.delete_todo(todo_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.init_db()
    app.run(debug=True)

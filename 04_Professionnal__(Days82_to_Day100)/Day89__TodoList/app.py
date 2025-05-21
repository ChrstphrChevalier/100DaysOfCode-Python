from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

DB_NAME = "todo.db"

def init_db():
    if not os.path.exists(DB_NAME):
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute("""
                CREATE TABLE tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content TEXT NOT NULL,
                    done INTEGER DEFAULT 0
                )
            """)

@app.route("/")
def index():
    conn = sqlite3.connect(DB_NAME)
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    content = request.form["content"]
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("INSERT INTO tasks (content, done) VALUES (?, 0)", (content,))
    return redirect(url_for("index"))

@app.route("/done/<int:task_id>")
def done(task_id):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete(task_id):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    return redirect(url_for("index"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)

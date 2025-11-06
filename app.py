from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(__file__), "notes.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_db()
    conn.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, content TEXT)")
    notes = conn.execute("SELECT * FROM notes ORDER BY id DESC").fetchall()
    return render_template("index.html", notes=notes)

@app.route("/add", methods=("GET", "POST"))
def add():
    if request.method == "POST":
        content = request.form["content"].strip()
        if content:
            conn = get_db()
            conn.execute("INSERT INTO notes (content) VALUES (?)", (content,))
            conn.commit()
        return redirect("/")
    return render_template("add.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

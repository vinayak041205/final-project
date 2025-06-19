# app.py
import os
from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from cs50 import SQL
from datetime import datetime

app = Flask(__name__)

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
if not os.path.exists("notes.db"):
    open("notes.db", "w").close()
db = SQL("sqlite:///notes.db")

# Create tables if not exist
db.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    hash TEXT NOT NULL
);
""")

db.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
""")

@app.route("/")
def index():
    if "user_id" not in session:
        return redirect("/login")
    notes = db.execute("SELECT * FROM notes WHERE user_id = ? ORDER BY id DESC", session["user_id"])
    return render_template("notes.html", notes=notes)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username or not password or not confirmation:
            return "Missing fields"
        if password != confirmation:
            return "Passwords must match"

        hash_pw = generate_password_hash(password)
        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash_pw)
        except:
            return "Username already exists"

        return redirect("/login")

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(user) != 1 or not check_password_hash(user[0]["hash"], password):
            return "Invalid username or password"

        session["user_id"] = user[0]["id"]
        return redirect("/")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        db.execute("INSERT INTO notes (user_id, title, content, created_at) VALUES (?, ?, ?, ?)",
                   session["user_id"], title, content, created_at)

        return redirect("/")

    return render_template("add_note.html")

@app.route("/delete/<int:note_id>")
def delete(note_id):
    db.execute("DELETE FROM notes WHERE id = ? AND user_id = ?", note_id, session["user_id"])
    return redirect("/")

@app.route("/edit/<int:note_id>", methods=["GET", "POST"])
def edit(note_id):
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        db.execute("UPDATE notes SET title = ?, content = ? WHERE id = ? AND user_id = ?",
                   title, content, note_id, session["user_id"])
        return redirect("/")

    note = db.execute("SELECT * FROM notes WHERE id = ? AND user_id = ?", note_id, session["user_id"])
    if not note:
        return "Note not found"
    return render_template("edit_note.html", note=note[0])

if __name__ == "__main__":
    app.run(debug=True)

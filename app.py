import os
import sqlite3
from datetime import datetime, timezone
from contextlib import closing
from functools import wraps
from flask import Flask, g, redirect, render_template, request, session, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-change-this-secret")
DATABASE = os.environ.get("DATABASE_PATH", "/data/social.db")

def connect_db():
    folder = os.path.dirname(DATABASE)
    if folder:
        os.makedirs(folder, exist_ok=True)
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with closing(connect_db()) as db, db:
        db.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL
        )""")
        db.execute("""CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            content TEXT NOT NULL CHECK(length(content) <= 280),
            created_at TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )""")

def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if "user_id" not in session:
            flash("Please sign in to do that.")
            return redirect(url_for("login"))
        return view(*args, **kwargs)
    return wrapped

@app.before_request
def ensure_db():
    init_db()

@app.route("/")
def index():
    with closing(connect_db()) as db, db:
        posts = db.execute("""SELECT posts.content, posts.created_at, users.username
            FROM posts JOIN users ON posts.user_id = users.id
            ORDER BY posts.id DESC""").fetchall()
    return render_template("index.html", posts=posts, username=session.get("username"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        if len(username) < 3 or len(username) > 30:
            flash("Username must be between 3 and 30 characters.")
        elif len(password) < 8:
            flash("Password must be at least 8 characters.")
        else:
            try:
                with closing(connect_db()) as db, db:
                    db.execute("INSERT INTO users(username, password_hash) VALUES (?, ?)",
                               (username, generate_password_hash(password)))
                flash("Account created. You can now sign in.")
                return redirect(url_for("login"))
            except sqlite3.IntegrityError:
                flash("That username is already taken.")
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        with closing(connect_db()) as db, db:
            user = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        if user and check_password_hash(user["password_hash"], password):
            session.clear()
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            return redirect(url_for("index"))
        flash("Invalid username or password.")
    return render_template("login.html")

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    flash("You have signed out.")
    return redirect(url_for("index"))

@app.route("/post", methods=["POST"])
@login_required
def create_post():
    content = request.form.get("content", "").strip()
    if not content:
        flash("Post cannot be empty.")
    elif len(content) > 280:
        flash("Posts must be 280 characters or fewer.")
    else:
        created_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        with closing(connect_db()) as db, db:
            db.execute("INSERT INTO posts(user_id, content, created_at) VALUES (?, ?, ?)",
                       (session["user_id"], content, created_at))
        flash("Your post has been published.")
    return redirect(url_for("index"))

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=False)

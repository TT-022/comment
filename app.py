import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Connect and create the table (only runs once)
def init_db():
    conn = sqlite3.connect("comments.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    conn = sqlite3.connect("comments.db")
    c = conn.cursor()

    if request.method == "POST":
        comment_text = request.form.get("comment")
        if comment_text:
            c.execute("INSERT INTO comments (text) VALUES (?)", (comment_text,))
            conn.commit()
        return redirect("/")

    c.execute("SELECT text FROM comments")
    comments = [row[0] for row in c.fetchall()]
    conn.close()
    return render_template("index.html", comments=comments)

if __name__ == "__main__":
    init_db()
    app.run(debug=True,host='0.0.0.0', port=int(os.environ.get('PORT', 5000)),use_reloader=False)

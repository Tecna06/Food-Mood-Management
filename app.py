# *** Simple , beginner friendly project written in python codes/SQL commands.



# --- 1: imports, moduls
from flask import Flask, render_template, request, redirect
import sqlite3


app = Flask(__name__)

# ---2:  connect database and table
def create_table():
    conn = sqlite3.connect("first_week.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS first_week (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            day TEXT,
            meal_time TEXT,
            appetite TEXT,
            food TEXT,
            emotions TEXT,
            hunger_level INTEGER,
            physical_signals TEXT
        )
    """)
    conn.commit()
    conn.close()


# --- 3: page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        day = request.form.get("day")
        meal_time = request.form.get("meal_time")
        appetite = request.form.get("appetite")
        food = request.form.get("food")
        emotions = request.form.get("emotions")
        hunger_level = request.form.get("hunger_level")
        physical_signals = request.form.get("physical_signals")

        conn = sqlite3.connect("first_week.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO first_week 
            (day, meal_time, appetite, food, emotions, hunger_level, physical_signals)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (day, meal_time, appetite, food, emotions, hunger_level, physical_signals))
        conn.commit()
        conn.close()

        return redirect("/")  # refresh page after save

    return render_template("form.html")

if __name__ == "__main__":
    create_table()
    app.run(debug=True)

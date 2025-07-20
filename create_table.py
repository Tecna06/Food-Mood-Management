# --- 1: imports
import sqlite3

# --- 2: connect databse
conn = sqlite3.connect("weekly_diary.db")
cursor = conn.cursor()

# Tablo
cursor.execute('''
CREATE TABLE IF NOT EXISTS first_week (
    day TEXT,
    meal_time TEXT,
    appetite TEXT,
    food TEXT,
    mood TEXT,
    hunger TEXT,
    physical_effect TEXT
)
''')

conn.commit()
conn.close()

print("✅ Table 'first_week' created successfully.")

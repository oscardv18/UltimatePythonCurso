import sqlite3

with sqlite3.connect("sqlite/app.db") as conn:
    cursor = conn.cursor()
    users = [(2, "Chachito Feliz"), (3, "Chanchito Triste")]
    cursor.executemany("INSERT INTO users VALUES(?, ?)", users)

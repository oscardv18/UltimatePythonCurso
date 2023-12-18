import sqlite3

with sqlite3.connect("sqlite/app.db") as conn:
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE if not exists users
        (id INTEGER primery key, name VARCHAR(50));
        """
    )

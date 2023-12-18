import sqlite3

conn = sqlite3.connect("sqlite/app.db")
cursor = conn.cursor()
cursor.execute(
    """
    CREATE TABLE if not exists users
    (id INTEGER primery key, name VARCHAR(50));
    """
)
conn.commit()
conn.close()

import sqlite3

conn = sqlite3.connect("tarefas.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tarefas (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               titulo TEXT,
               concluida INTEGER
)
""")

conn.commit()
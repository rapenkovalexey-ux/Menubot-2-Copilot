import sqlite3

conn = sqlite3.connect("data.db", check_same_thread=False)

conn.execute("""
CREATE TABLE IF NOT EXISTS preferences (
    user_id INTEGER PRIMARY KEY,
    prefs TEXT
)
""")
conn.commit()


def save_prefs(user_id: int, prefs: str):
    conn.execute(
        "REPLACE INTO preferences (user_id, prefs) VALUES (?, ?)",
        (user_id, prefs)
    )
    conn.commit()


def load_prefs(user_id: int):
    row = conn.execute(
        "SELECT prefs FROM preferences WHERE user_id = ?",
        (user_id,)
    ).fetchone()
    return row[0] if row else None

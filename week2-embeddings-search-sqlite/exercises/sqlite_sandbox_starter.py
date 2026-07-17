"""Week 2 exercise: SQLite basics.

Goal: create a table, insert rows, and query them — using only Python's
built-in sqlite3 module (nothing to install). Replace each `...` in
main() following these steps, then run:

    python sqlite_sandbox_starter.py

Steps (each matches one `...` below, in order):
1. Create a table called documents with three columns:
   id INTEGER PRIMARY KEY, source TEXT NOT NULL, content TEXT NOT NULL.
   Hint: db.execute("CREATE TABLE IF NOT EXISTS ...")
2. Insert at least three rows using ? placeholders:
   db.execute("INSERT INTO documents (source, content) VALUES (?, ?)", (...))
   Remember db.commit() afterwards!
3. Fetch and print the row with id 2.
   Hint: db.execute("SELECT ... WHERE id = ?", (2,)).fetchone()
4. Fetch and print all rows whose content contains a keyword, using LIKE
   with a % wildcard.

Think about it afterwards: LIKE only matches literal text. What kind of
question would keyword search miss that embedding search (this week's
other exercise) would catch?
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "sandbox.db"


def main():
    db = sqlite3.connect(DB_PATH)

    ...

    ...

    ...

    ...

    db.close()


if __name__ == "__main__":
    main()

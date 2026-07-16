"""Week 2 exercise: SQLite basics.

Goal: create a table, insert rows, and query them — using only Python's
built-in sqlite3 module (nothing to install).

Fill in the TODOs, then run:  python sqlite_sandbox_starter.py
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "sandbox.db"


def main():
    db = sqlite3.connect(DB_PATH)

    # TODO 1: create a table called documents with three columns:
    #   id      INTEGER PRIMARY KEY
    #   source  TEXT NOT NULL
    #   content TEXT NOT NULL
    # Hint: db.execute("CREATE TABLE IF NOT EXISTS ...")
    ...

    # TODO 2: insert at least three rows using ? placeholders:
    #   db.execute("INSERT INTO documents (source, content) VALUES (?, ?)", (...))
    # Remember db.commit() afterwards!
    ...

    # TODO 3: fetch and print the row with id 2.
    # Hint: db.execute("SELECT ... WHERE id = ?", (2,)).fetchone()
    ...

    # TODO 4: fetch and print all rows whose content contains a keyword,
    # using LIKE with a % wildcard.
    ...

    db.close()

    # Think about it: LIKE only matches literal text. What kind of question
    # would keyword search miss that embedding search (this week's other
    # exercise) would catch?


if __name__ == "__main__":
    main()

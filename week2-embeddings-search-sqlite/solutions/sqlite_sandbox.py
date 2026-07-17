"""Week 2: first steps with SQLite — the database that is just a file.

    python sqlite_sandbox.py

Creates sandbox.db next to this script; delete the file to start over.

What the script does, in order:
1. Creates a documents table (IF NOT EXISTS makes re-runs safe).
2. Inserts a few rows using ? placeholders, which keep data and SQL
   separate, then commits. It clears the table first so every run starts
   clean.
3. Fetches one row by id.
4. Fetches rows by keyword with LIKE. Note that LIKE only finds literal
   text — it would miss a question like "how long is the guarantee?".
   Next week the same table gains an embedding column so we can search by
   MEANING instead.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "sandbox.db"


def main():
    db = sqlite3.connect(DB_PATH)

    db.execute(
        """
        CREATE TABLE IF NOT EXISTS documents (
            id      INTEGER PRIMARY KEY,
            source  TEXT NOT NULL,
            content TEXT NOT NULL
        )
        """
    )

    db.execute("DELETE FROM documents")
    rows = [
        ("manual.md", "Hold the steam button for five seconds to prime the pump."),
        ("faq.md", "Replace the water filter cartridge every two months."),
        ("warranty.md", "Every machine carries a two-year limited warranty."),
    ]
    db.executemany("INSERT INTO documents (source, content) VALUES (?, ?)", rows)
    db.commit()

    row = db.execute("SELECT source, content FROM documents WHERE id = 2").fetchone()
    print("Row with id 2:", row)

    matches = db.execute(
        "SELECT source FROM documents WHERE content LIKE ?", ("%warranty%",)
    ).fetchall()
    print("Documents mentioning 'warranty':", matches)

    db.close()
    print(f"\nAll data lives in one file: {DB_PATH.name}")


if __name__ == "__main__":
    main()

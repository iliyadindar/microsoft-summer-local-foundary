"""Week 2: first steps with SQLite — the database that is just a file.

    python sqlite_sandbox.py

Creates sandbox.db next to this script. Delete the file to start over.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "sandbox.db"


def main():
    db = sqlite3.connect(DB_PATH)

    # 1. Create a table (IF NOT EXISTS makes re-runs safe).
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS documents (
            id      INTEGER PRIMARY KEY,
            source  TEXT NOT NULL,
            content TEXT NOT NULL
        )
        """
    )

    # 2. Insert a few rows. The ? placeholders keep data and SQL separate.
    db.execute("DELETE FROM documents")  # start clean on every run
    rows = [
        ("manual.md", "Hold the steam button for five seconds to prime the pump."),
        ("faq.md", "Replace the water filter cartridge every two months."),
        ("warranty.md", "Every machine carries a two-year limited warranty."),
    ]
    db.executemany("INSERT INTO documents (source, content) VALUES (?, ?)", rows)
    db.commit()

    # 3. Query by id.
    row = db.execute("SELECT source, content FROM documents WHERE id = 2").fetchone()
    print("Row with id 2:", row)

    # 4. Query by keyword. LIKE only finds literal text — it would miss a
    #    question like "how long is the guarantee?". Next step: store
    #    embeddings in this table so we can search by MEANING instead.
    matches = db.execute(
        "SELECT source FROM documents WHERE content LIKE ?", ("%warranty%",)
    ).fetchall()
    print("Documents mentioning 'warranty':", matches)

    db.close()
    print(f"\nAll data lives in one file: {DB_PATH.name}")


if __name__ == "__main__":
    main()

"""SQLite setup: connection helper + schema init + one-time seeding.

This is the plumbing. The per-endpoint queries (SELECT/INSERT/DELETE) live in
the routes — that's the part you write.
"""

import sqlite3
from pathlib import Path

from app.seed_data import SAMPLES

# The DB is a single file living next to this module.
DB_PATH = Path(__file__).parent / "samples.db"


def get_connection() -> sqlite3.Connection:
    """Open a connection to the samples DB.

    `row_factory = sqlite3.Row` makes rows behave like dicts — you can do
    `row["rock_type"]` and `dict(row)` instead of unpacking tuples by index.
    Open one of these per request, use it, then close it.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    """Create the table if it doesn't exist, and seed it once (if empty).

    Called once on app startup. Idempotent: safe to run every boot — the
    CREATE uses IF NOT EXISTS and seeding is gated on an empty table.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS samples (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            name      TEXT NOT NULL,
            rock_type TEXT NOT NULL,
            grade     REAL NOT NULL,
            depth_m   REAL NOT NULL
        )
        """
    )

    # Seed only if the table is currently empty (don't duplicate on restart).
    existing = cursor.execute("SELECT COUNT(*) FROM samples").fetchone()[0]
    if existing == 0:
        cursor.executemany(
            "INSERT INTO samples (name, rock_type, grade, depth_m) VALUES (?, ?, ?, ?)",
            [(s["name"], s["rock_type"], s["grade"], s["depth_m"]) for s in SAMPLES],
        )

    conn.commit()
    conn.close()

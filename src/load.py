import sqlite3

def load_to_db(df, db_path="data/mentah/reviews.db"):
    import sqlite3
    conn = sqlite3.connect(db_path)

    # append dulu
    df.to_sql("reviews", conn, if_exists="append", index=False)

    # dedup berdasarkan text (simple)
    conn.execute("""
        DELETE FROM reviews
        WHERE rowid NOT IN (
            SELECT MIN(rowid)
            FROM reviews
            GROUP BY text
        )
    """)
    conn.commit()
    conn.close()

    print("✅ Data appended & deduplicated")
import sqlite3
import pandas as pd

conn = sqlite3.connect("data/mentah/reviews.db")

query = "SELECT sentiment, COUNT(*) as total FROM reviews GROUP BY sentiment"
df = pd.read_sql(query, conn)

print(df)

conn.close()
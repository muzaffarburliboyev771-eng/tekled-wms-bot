
import sqlite3

conn = sqlite3.connect("wms.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT,
    location TEXT,
    location_code TEXT UNIQUE
)
""")

cur.execute("""
CREATE INDEX IF NOT EXISTS idx_code ON products (location_code)
""")

conn.commit()
conn.close()

print("✅ Database tayyor")

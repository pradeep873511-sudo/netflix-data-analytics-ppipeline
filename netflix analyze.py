import sqlite3
import pandas as pd

conn = sqlite3.connect("netflix.db")

q1 = "SELECT type, COUNT(*) as count FROM netflix GROUP BY type"
print(pd.read_sql(q1, conn))

q2 = """
SELECT country, COUNT(*) as count 
FROM netflix 
WHERE country != 'Unknown'
GROUP BY country 
ORDER BY count DESC 
LIMIT 10
"""
print(pd.read_sql(q2, conn))

q3 = """
SELECT strftime('%Y', date_added) as year, COUNT(*) as count
FROM netflix
GROUP BY year
ORDER BY year
"""
print(pd.read_sql(q3, conn))

conn.close()
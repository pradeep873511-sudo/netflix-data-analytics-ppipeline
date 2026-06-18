import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("netflix.db")

plt.style.use('seaborn-v0_8')

# 1. Movies vs TV Shows
q1 = "SELECT type, COUNT(*) as count FROM netflix GROUP BY type"
df1 = pd.read_sql(q1, conn)

plt.figure(figsize=(6,4))
plt.bar(df1['type'], df1['count'], color=['#FF6B6B', '#4ECDC4'])
plt.title('Movies vs TV Shows')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()

# 2. Top 10 Countries
q2 = """
SELECT country, COUNT(*) as count 
FROM netflix 
WHERE country != 'Unknown'
GROUP BY country 
ORDER BY count DESC 
LIMIT 10
"""
df2 = pd.read_sql(q2, conn)

plt.figure(figsize=(8,5))
plt.barh(df2['country'], df2['count'], color='#6C5CE7')
plt.title('Top 10 Countries by Content')
plt.xlabel('Count')
plt.ylabel('Country')
plt.gca().invert_yaxis()
plt.show()

# 3. Content Added Per Year
q3 = """
SELECT strftime('%Y', date_added) as year, COUNT(*) as count
FROM netflix
GROUP BY year
ORDER BY year
"""
df3 = pd.read_sql(q3, conn)

plt.figure(figsize=(8,5))
plt.plot(df3['year'], df3['count'], marker='o', color='#FFD93D', linewidth=2)
plt.title('Content Added Per Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

conn.close()
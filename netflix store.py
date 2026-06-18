import pandas as pd
import sqlite3

df = pd.read_csv("netflix_titles.csv")

df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Unknown")
df['country'] = df['country'].fillna("Unknown")
df = df.dropna(subset=['date_added', 'rating', 'duration'])
df['date_added'] = pd.to_datetime(df['date_added'], format='mixed')

conn = sqlite3.connect("netflix.db")
df.to_sql("netflix", conn, if_exists="replace", index=False)
conn.close()

print("Data stored successfully in netflix.db")
import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("netflix.db")

st.title("Netflix Data Analytics Dashboard")
st.write("Explore Netflix content data (2008-2021)")

st.subheader("Movies vs TV Shows")
q1 = "SELECT type, COUNT(*) as count FROM netflix GROUP BY type"
df1 = pd.read_sql(q1, conn)

fig1, ax1 = plt.subplots()
ax1.bar(df1['type'], df1['count'], color=['#FF6B6B', '#4ECDC4'])
ax1.set_xlabel('Type')
ax1.set_ylabel('Count')
st.pyplot(fig1)

st.subheader("Top 10 Countries by Content")
q2 = """
SELECT country, COUNT(*) as count 
FROM netflix 
WHERE country != 'Unknown'
GROUP BY country 
ORDER BY count DESC 
LIMIT 10
"""
df2 = pd.read_sql(q2, conn)

fig2, ax2 = plt.subplots()
ax2.barh(df2['country'], df2['count'], color='#6C5CE7')
ax2.set_xlabel('Count')
ax2.invert_yaxis()
st.pyplot(fig2)

st.subheader("Content Added Per Year")
q3 = """
SELECT strftime('%Y', date_added) as year, COUNT(*) as count
FROM netflix
GROUP BY year
ORDER BY year
"""
df3 = pd.read_sql(q3, conn)

fig3, ax3 = plt.subplots()
ax3.plot(df3['year'], df3['count'], marker='o', color='#FFD93D', linewidth=2)
ax3.set_xlabel('Year')
ax3.set_ylabel('Count')
plt.setp(ax3.get_xticklabels(), rotation=45)
st.pyplot(fig3)

st.subheader("Search Netflix Title")
search = st.text_input("Enter a title to search:")
if search:
    q4 = f"SELECT title, type, country, release_year, rating FROM netflix WHERE title LIKE '%{search}%'"
    df4 = pd.read_sql(q4, conn)
    st.dataframe(df4)

conn.close()
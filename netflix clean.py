import pandas as pd

df = pd.read_csv("netflix_titles.csv")

df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Unknown")
df['country'] = df['country'].fillna("Unknown")

df = df.dropna(subset=['date_added', 'rating', 'duration'])

df['date_added'] = pd.to_datetime(df['date_added'], format='mixed')

print(df.isnull().sum())   
print(df.shape)           
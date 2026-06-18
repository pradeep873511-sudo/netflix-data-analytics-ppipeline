import pandas as pd

df = pd.read_csv("netflix_titles.csv")

print(df.shape)        
print(df.columns)        
print(df.head())         
print(df.info())         
print(df.isnull().sum())
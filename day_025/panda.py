import pandas as pd
import numpy as np

df = pd.read_csv('hacker_news.csv')
df

# print(first_5_rows)
first_5_rows = df.head()

# print(last_5_rows)
last_5_rows = df.tail()

# print(title_series)
title_series = df.iloc[:,2]


print(df.shape)

python_title = df.loc[df['title'].str.contains('Python', case=False)]
print(python_title)

js_title = df.loc[df['title'].str.contains('JavaScript', case=False)]
print(js_title)

print(df.describe())
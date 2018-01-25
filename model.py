import pandas as pd

df = pd.read_csv('stockoverview.csv')
df = df.sort_values(df.columns[0])
df.to_csv('new_stockoverview.csv', encoding='utf-8', sep=',', index=False)

print df.info()
print df.describe()

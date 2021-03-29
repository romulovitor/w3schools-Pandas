import pandas as pd

df = pd.read_csv('data.csv')

# Converter para data:
df['Date'] = pd.to_datetime(df['Date'])

# Remova as linhas com um valor NULL na coluna "Data":
df.dropna(subset=['Date'], inplace = True)

print(df.to_string())

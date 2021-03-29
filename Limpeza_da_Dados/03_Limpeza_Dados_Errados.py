import pandas as pd

df = pd.read_csv('data.csv')

# Uma maneira de corrigir valores errados é substituí-los por outra coisa.
df.loc[55, 'idade'] = 99

print(df.to_string(), '\n')

# Faça um loop por todos os valores na coluna "idade".
df = pd.read_csv('data.csv')

for x in df.index:
    if df.loc[x, 'idade'] > 50:
        df.loc[x, 'idade'] = 18

df.dropna(inplace=True)

print(df.to_string(), '\n')

# Exclua as linhas em que a "idade" seja superior a 120:
for x in df.index:
    if df.loc[x, 'idade'] == 18:
        df.drop(x, inplace=True)

print(df.to_string(), '\n')
import pandas as pd

# Crie um DataFrame simples do Pandas:
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

print(df, '\n')

# consulte o índice da linha
print(df.loc[0], '\n')

# Retorne as linhas 0 e 1:
print(df.loc[[0, 1]], '\n')

# Índices Nomeados
df = pd.DataFrame(data, index=['day1', 'day2', 'day3'])
print(df, '\n')

# Localizar índices nomeados
print(df.loc['day2'])
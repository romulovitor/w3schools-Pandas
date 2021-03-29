import pandas as pd

df = pd.read_csv('data.csv')

# Retorne um novo quadro de dados sem células vazias:
new_df = df.dropna()

print(new_df.to_string(), '\n')


# Remova todas as linhas com valores NULL:
df = pd.read_csv('data.csv')

df.dropna(inplace=True)

print(df.to_string(), '\n')


# Substituir Valores Vazios
df = pd.read_csv('data.csv')

df.fillna('VALOR_NULL', inplace=True)
print(df.to_string(), '\n')

# Substituir apenas por colunas especificadas
df = pd.read_csv('data.csv')

df['idade'].fillna(0, inplace=True)

print(df.to_string(), '\n')


# Substitua usando média, mediana ou modo
df = pd.read_csv('data.csv')

media = df["idade"].mean()

df['idade'].fillna(media, inplace=True)
print(df.to_string(), '\m')


# Calcule o MODO e substitua quaisquer valores vazios por ele:
# Modo = o valor que aparece com mais frequência.
df = pd.read_csv('data.csv')

x = df["idade"].mode()[0]

df["idade"].fillna(x, inplace = True)
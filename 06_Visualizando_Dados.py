import pandas as pd

df = pd.read_csv('data.csv')

# se o número de linhas não for especificado, o head()método retornará as 5 primeiras linhas.
print(df.head(5), '\n')

# O tail()método retorna os cabeçalhos e um número especificado de linhas, começando da parte inferior.
print(df.tail(), '\n')

# O objeto DataFrames possui um método chamado info(), que fornece mais informações sobre o conjunto de dados.
print(df.info())

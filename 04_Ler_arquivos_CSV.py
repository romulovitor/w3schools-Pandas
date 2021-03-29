import pandas as pd

# Uma maneira simples de armazenar conjuntos de big data é usar arquivos CSV (arquivos separados por vírgula).
df = pd.read_csv('data.csv')

# use to_string() para imprimir todos os DataFrame.
print(df.to_string())

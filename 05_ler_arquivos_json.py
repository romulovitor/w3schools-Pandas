import pandas as pd

# Uma maneira simples de armazenar conjuntos de big data é usar arquivos JSON.
df = pd.read_json('data.json')

# use to_string() para imprimir todos os DataFrame.
print(df.to_string())

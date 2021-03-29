import pandas as pd

# Lembre-se: o (inplace = True)fará com que o método NÃO retorne um novo DataFrame, mas removerá todas as duplicatas
# do DataFrame original .
df = pd.read_csv('data_duplicada.csv')

df.drop_duplicates(inplace=True)
print(df.to_string())

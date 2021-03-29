import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot(kind='bar', y='idade', x='nome')

plt.show()

# Apenas vendo diferentes funções de manipulação de tabelas com pandas

import pandas as pd

df = pd.read_csv('tabela.csv', encoding='latin1', sep=';')

df.groupby('Nome')

print(df)

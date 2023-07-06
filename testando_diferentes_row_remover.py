# Catalogando diferentes maneiras de manipular tabelas - funções para remover linhas

import pandas as pd
import numpy

data = {'Produto': ['pote de chimia', 'pasta de amendoim', 'pao de forma', 'cafe soluvel'], 'Valor': [8, 18, 6, 5]}
tabela = pd.DataFrame(data)
print(tabela)


# Remover linhas com base em uma string específica na coluna 'Produto'

# opção 1
tabela = tabela.drop(tabela[tabela['Produto'] == 'pote de chimia'].index)
print(f'\n\n{tabela}')

#opção 2
tabela = tabela[~(tabela['Produto'] == 'pasta de amendoim')]
print(f'\n\n{tabela}')


# Remover linhas com base em uma string específica independente da coluna

#opção 1
tabela = tabela.replace('pao de forma', numpy.nan)
tabela = tabela.dropna()
print(f'\n\n{tabela}')

#opção 2
tabela = tabela[~tabela.apply(lambda row: row.astype(str).str.contains('cafe soluvel').any(), axis=1)]
print(f'\n\n{tabela}\n\nEncerrado :D')

# Arquivo utilizado para testar funções de outro software, circula através do
# dir csv_file_testing e separa dentro de um dict contendo os nomes e períodos

import os

os.chdir(r'csv_file_testing/')
# for file in os.listdir():
#     print(file)

csvs = []

# csv names loop
for i in os.listdir():
    csvs.append(i)

periods = []

# year separation loop
for i in os.listdir():
    i = i.split('.')
    i = i[0].split('_')
    if i[-1] not in periods:
        if i[-1] != 'documentacao':
            periods.append(i[-1])


print({'file': csvs, 'period': periods})

# Estudando a biblioteca glob utilizando o dir csv_file_testing

import glob

files_from = glob.glob('csv_file_testing/*data*')

for file in files_from:
    print(file)

for file in files_from:
    print(file.split('\\')[1])

print(files_from)

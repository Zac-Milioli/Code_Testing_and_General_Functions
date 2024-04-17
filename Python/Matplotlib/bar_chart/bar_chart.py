# Documentação https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar

from matplotlib import pyplot as plt
import numpy as np

# print(plt.style.available)

plt.style.use('seaborn-v0_8-dark')
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# Para poder colocar uma barra ao lado da outra, sem overlaping, é necessário
# fazer algumas ações usando numpy. É criada uma lista de indexes usando como base
# o tamanho da lista utilizada no eixo X. Após isso, serão alterados os valores de
# x a cada utilização do eixo, colocando a próxima barra ao lado da outra.
# É necessário saber a largura das barras para indicar quanto será necessário
# mover as barras entre o eixo X.
# Aqui é criado um array contendo o mesmo número de itens que a lista de idades
x_indexes = np.arange(len(ages_x))
width = 0.25
# Este item é então usado no lugar do ages_x durante a construção dos charts


# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
plt.bar(x_indexes - width, py_dev_y, width=width, label='Python')
# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
plt.bar(x_indexes + width, js_dev_y, width=width, label="JavaScript")
# Median Developer Salaries by Age
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
plt.bar(x_indexes, dev_y, width=width, label='Todos os devs')

plt.xlabel("Idade")
plt.ylabel("Média salarial")
plt.title("Salário médio por idade em 2019 (USD)")

# Aqui é alterada a legenda que aparece abaixo do eixo x. Como ele foi alterado
# anteriormente para o ajuste de barras, é necessário alterar ele novamente para
# leitura correta dos dados. Isso se faz passando uma lista contendo os eixos a serem
# alterados, seguido dos novos labels que substituirão estes.
plt.xticks(ticks=x_indexes, labels=ages_x)

plt.legend()
plt.savefig(r"Python/Matplotlib/bar_chart/simple_bar_chart.png")
plt.show()
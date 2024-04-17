# Documentação https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot

from matplotlib import pyplot as plt

# Atributo que exibe os estilos padrão estão disponíveis
# print(plt.style.available)

#  Os estilos possuem suas cores, linewidths e grids próprios. Os parâmetros que são especificados
# nas funções de criação de plot sobrepões os padrões do estilo escolhido.
plt.style.use('seaborn-v0_8-pastel')

# Método que altera todo o estilo do plot para ficar cartunesco
# plt.xkcd()

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# A ordem dos plots é a ordem em que são colocados na tela. Em layers

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
# plt.plot(ages_x, py_dev_y, color="#00FF5F", linestyle=':', linewidth=2, label='Python')
plt.plot(ages_x, py_dev_y, linestyle=':', linewidth=2, label='Python')

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
# plt.plot(ages_x, js_dev_y, color="#00FFC8", linestyle='--', label="JavaScript")
plt.plot(ages_x, js_dev_y, linestyle='--', label="JavaScript")

# Median Developer Salaries by Age
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
# plt.plot(ages_x, dev_y, color="#3700FF", linestyle='-', marker='.', label='Todos os devs')
plt.plot(ages_x, dev_y, linestyle='-', marker='.', label='Todos os devs')

# Define nomes e títulos
plt.xlabel("Idade")
plt.ylabel("Média salarial")
plt.title("Salário médio por idade em 2019 (USD)")

# Adicionar legenda no plot:
# Inserir na ordem em que foram adicionados ao plot
# plt.legend(["Todos os devs", "Python"])
# mesmo que sejam passados labels dentro de cada plot, é necessário criar o legend para adicionar na tela
plt.legend()

# Adiciona grid no gráfico
plt.grid(True)

# Método para ajeitar o gráfico para caber em telas menores
plt.tight_layout()

# Salva o gráfico
plt.savefig(r"Python/Matplotlib/plot/simple_plot.png")

plt.show()

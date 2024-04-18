# Documentação https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stackplot.html#matplotlib.pyplot.stackplot

from matplotlib import pyplot as plt

plt.style.use('dark_background')

# Data
minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]
labels = ['player 1', 'player 2', 'player 3']
colors = ["#0F00FF", '#FF00D8', '#00FFCA']

# o primeiro item equivalerá ao X, seguido dos itens a serem plotados baseado no range das próprias listas
plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)
# sempre usar o método legend para aplicar a legenda(labels) na tela
# a posição pode ser definida
plt.legend(loc='upper right')

plt.xlabel("Minutos")
plt.ylabel("Pontuação")
plt.title("StackPlot")
plt.grid(True)
plt.tight_layout()
plt.savefig(r"Python/Matplotlib/stack_plot/simple_stack_plot.png")
plt.show()

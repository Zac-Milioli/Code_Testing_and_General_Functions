# Documentação https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter

from matplotlib import pyplot as plt
import pandas as pd
plt.style.use('seaborn-v0_8-dark')



# x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
# y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]

# # Esta lista é passada como argumento de c para representar as cores a serem usadas nos pontos seguindo a ordem
# colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]

# # Esta lista é passada no argumento sizes para indicar que os pontos devem ter tamanhos diferentes, seguindo a ordem
# sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174, 538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]

# # s é o tamanho dos pontos (pode ser uma lista)
# # c é a cor do marcador (pode ser uma lista). Pode ser usado um cmap como argumento https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
# plt.scatter(x, y, s=sizes, c=colors, cmap='Greens', marker='v', edgecolor='black', linewidth=1, alpha=0.5)

# # É adicionado uma barra em gradiente com as cores como legenda
# cbar = plt.colorbar()
# cbar.set_label("Nível de satisfação")

data = pd.read_csv(r'Python/Matplotlib/scatter_plot/2019-05-31-data.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(view_count, likes, c=ratio, cmap='summer', edgecolors='black', linewidth=1, alpha=0.5)

# Definindo a escala do plot
plt.xscale('log')
plt.yscale('log')

cbar = plt.colorbar()
cbar.set_label('Like/Dislike Ratio')

plt.title('Videos na página trending do YouTube')
plt.xlabel('Visualizações')
plt.ylabel('Likes')
plt.grid(True)
plt.tight_layout()
plt.savefig(r"Python/Matplotlib/scatter_plot/simple_scatter_plot.png")
plt.show()

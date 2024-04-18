# Documentação https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html#matplotlib.pyplot.pie

from matplotlib import pyplot as plt

plt.style.use('seaborn-v0_8-dark')

# fatias = [150, 40, 35, 12]
# labels = ["150", "40", '35', '12']
# colors = ["#46B9AD", '#C33C91', '#A3CC33', '#001191']

# Language Popularity
# slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
# labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']

# valores explodidos são exibidos mais evidentemente no pie chart, separados do gráfico. É representado por porcentagem do raio
explode = [0, 0, 0, 0.1, 0]

# Wedgeprops é um dicionário contendo configurações específicas para a torta. Vide a documentação de wedgedrops
# Shadow é um argumento extra que adiciona sombrinha no gráfico
# startangle é um argumento que define a quantos graus o matplotlib deve começar a plotar os itens. Rotação
# autopct é um argumento que exibe a porcentagem de cada fatia, no formato especificado pelo usuário seguindo documentação
plt.pie(slices, labels=labels, explode=explode, shadow=True, startangle=90, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})

plt.title("Gráfico importantíssimo")
plt.tight_layout()
plt.savefig(r"Python/Matplotlib/pie_chart/simple_pie_chart.png")
plt.show()


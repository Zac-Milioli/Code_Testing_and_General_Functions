# Documentação https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html#matplotlib.pyplot.pie

from matplotlib import pyplot as plt

plt.style.use('seaborn-v0_8-dark')

fatias = [85, 15]
labels = ["Pedaço maior azul", "Pedaço menor laranja"]

# Wedgeprops é um dicionário contendo configurações específicas para a torta
# Documentação: 
plt.pie(fatias, labels=labels, wedgeprops={'edgecolor': 'black'})

plt.title("Gráfico importantíssimo")
plt.tight_layout()
plt.savefig(r"Python/Matplotlib/pie_chart/simple_pie_chart.png")
plt.show()


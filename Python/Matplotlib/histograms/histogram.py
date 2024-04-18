# Documentação https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist

from matplotlib import pyplot as plt
import pandas as pd
plt.style.use('seaborn-v0_8-pastel')

# ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
# Ranges que não são incluídos na lista são excluídos do histograma
# bins = [10,20,30,40,50,60]

df = pd.read_csv(r'Python/Matplotlib/histograms/data.csv')
ids = df['Responder_id']
age = df['Age']
media = 29
# bins = [10,20,30,40,50,60,70,80,90,100]
bins = range(10,100,10)

# O parâmetro log torna os valores em log. Pode tornar melhor a visualização entre valores com grande diferença
# Ex.: 1000 -> 10²
plt.hist(age, bins=bins, edgecolor="black", log=True)

# O histograma agrupa os dados em "bins", portanto é necessário definir o número de bins
# Pode ser usado um número ou uma lista
# plt.hist(ages, bins=5, edgecolor="black")
# plt.hist(ages, bins=bins, edgecolor="black")

# axvline serve para aplicar um traço em um ponto específico de X
plt.axvline(media, label='Idade média', color='red', linewidth=2)

plt.title('Idade dos participantes')
plt.xlabel('Idade')
plt.ylabel('Respostas')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(r"Python/Matplotlib/histograms/simple_histogram.png")
plt.show()

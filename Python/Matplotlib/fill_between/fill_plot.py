# Documentação https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill_between.html#matplotlib.pyplot.fill_between

from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('seaborn-v0_8-pastel')

df = pd.read_csv(r'Python/Matplotlib/fill_between/data.csv')
ages = df["Age"]
all_dev = df["All_Devs"]
py_dev = df["Python"]

plt.plot(ages, all_dev, label="All devs")
plt.plot(ages, py_dev, label="Python", linestyle=":")

media = 57287

# Funciona colocando os pares de preenchimento, na ordem de um para o outro respectivamente
# Alpha equivale a opacidade, em porcentagem
# Ao não inserir um terceiro valor, o gráfico terpa preenchida a área completa partindo do 0
# Ao preencher o terceiro parâmetro é delimitada uma nova "altura" para o fill
# O parâmetro where serve para adicionar condições para o fill acontecer / onde acontecer
# O método interpolate serve para garantir que as regiões tenham seu fill feito corretamente
# e outras regiões não sejam cortadas
plt.fill_between(ages, py_dev, all_dev, where=(py_dev > all_dev), interpolate=True, alpha=0.25, label="Acima da média")
plt.fill_between(ages, py_dev, all_dev, where=(py_dev <= all_dev), interpolate=True, alpha=0.25, label="Abaixo da média")


plt.xlabel("Idade")
plt.ylabel("Média salarial")
plt.title("Salário médio por idade em 2019 (USD)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(r"Python/Matplotlib/fill_between/simple_fill_plot.png")
plt.show()

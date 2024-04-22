# Documentação https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.subplot.html

import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('dark_background')

# A função gcf serve para retornar a figura atual
# A função gca serve para retornar os axis atuais


data = pd.read_csv(r'Python/Matplotlib/subplots/data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

# Retorna a figura e axis atuais. É o mesmo que fazer fig = gcf() e ax = gca()
# O ax pode ser entendido como "gráfico" específico. fig é a janela ou objeto.
# O nrows e ncols serve para construir o posicionamento dos plots na janela, seu retorno
# é uma lista em formato de matriz contendo os plots e suas devidas posições
# O parâmetro sharex e sharey serve para remover a informação do seu axis especifico em um dos
# plots
# O método subplots pode ser executado mais de uma vez para gerar múltiplas figs, assim,
# aparecerão múltiplas janelas com cada subplot ao invés de apenas uma
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

ax1.plot(ages, py_salaries, label='Python')
ax1.plot(ages, js_salaries, label='JavaScript')

ax2.plot(ages, dev_salaries, label='All Devs')

ax1.legend()
ax2.legend()

# Quando se trabalha com subplots estes parâmetros recebem o termo set_, pois assim é aplicado por plot
ax1.set_title('Median Salary (USD) by Age')
ax1.set_ylabel('Median Salary (USD)')
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')
ax1.grid(True)
ax2.grid(True)

fig.tight_layout()
fig.savefig(r'Python/Matplotlib/subplots/simple_subplot.png')


# criando um exemplo para mostrar os diferentes posicionamentos de subplots
fig2, axs = plt.subplots(nrows=2, ncols=2)
fig2.suptitle("Matriz de plots")
axs[0,0].set_facecolor("green")
axs[0,1].set_facecolor("blue")
axs[1,0].set_facecolor("yellow")
axs[1,1].set_facecolor("red")
fig2.savefig(r'Python/Matplotlib/subplots/matriz_subplot.png')

plt.show()
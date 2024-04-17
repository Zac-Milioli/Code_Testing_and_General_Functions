from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter

plt.style.use('seaborn-v0_8-dark')

df = pd.read_csv(r"Python/Matplotlib/bar_chart/data.csv", sep=',')
id_list = df["Responder_id"]
langs_list = df['LanguagesWorkedWith']

# O contador construirá um dict onde serão contadas quantas vezes cada linguagem aparece 
counter = Counter()

# Aqui é percorrida toda a coluna LanguagesWorkedWith e atualiza o contador transformando
# as repostas do dataframe em listas
for language in langs_list:
    counter.update(language.split(";"))

languages = []
popularity = []

# o método most_common retorna uma lista de tuplas contendo os top X valores mais comuns
# ex: [(Zac, 20), (Python, 15), (Ruby, 10), (JavaScript, 5), (Java, 2)]
for i in counter.most_common(15):
    languages.append(i[0])
    popularity.append(i[1])

# Para tornar o gráfico mais visualmente agradável, com as barras maiores em cima e as menores
# em baixo, basta inverter os valores das listas
languages.reverse()
popularity.reverse()

# plt.bar(languages, popularity)
# O método barh inverte o x e o y, simplesmente
plt.barh(languages, popularity)

plt.title("Linguagens mais populares de 2019")
plt.xlabel("Número de usuários")

plt.tight_layout()
plt.savefig(r"Python/Matplotlib/bar_chart/simple_bar_chart_from_csv.png")
plt.show()
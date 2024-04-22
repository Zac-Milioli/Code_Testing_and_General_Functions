# Documentação https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.animation.FuncAnimation.html

from matplotlib import pyplot as plt
import pandas as pd
import random
from itertools import count
from matplotlib.animation import FuncAnimation

plt.style.use("seaborn-v0_8-dark")

x = []
y = []

# Cria um contador
index = count()

# # É necessário passar 1 argumento para a função que será executada pelo FuncAnimation por causa da forma que o mesmo funciona
# def animate(i):
#     # a função next vai apenas incrementar o contador por 1 a cada iteração
#     x.append(next(index))
#     y.append(random.randint(0, 5))
#     # O método cla serve para limpar todos os axis, excluir as informações antigas
#     # Isso é necessário pois se não for feito serão criadas várias linhas novas por
#     # cima uma da outra a cada iteração.
#     plt.cla()
#     plt.plot(x, y)
#     plt.grid(True)
#     plt.tight_layout()
#     plt.savefig(r"Python/Matplotlib/live_data/simple_live_data.png")

def animate(i):
    df = pd.read_csv(r"Python/Matplotlib/live_data/data.csv")
    x = df['x_value']
    y1 = df['total_1']
    y2 = df['total_2']

    plt.cla()
    plt.plot(x, y1, label='Canal 1')
    plt.plot(x, y2, label='Canal 2')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(r"Python/Matplotlib/live_data/simple_live_data.png")


# Para a construção da função FuncAnimation é necessário passar a figura, a função a ser executada por iteração e o intervalo em ms
# Caso seja necessário passar mais argumentos à função de iteração, o FuncAnimation possui o parâmetro fargs onde podem ser depositados
# esses valores. Somado a isso, também existe o parâmetro init para caso seja necessário executar uma função de inicialização
# antes da função principal
ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.show()

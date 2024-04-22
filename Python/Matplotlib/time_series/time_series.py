# Documentação https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.plot_date.html

from matplotlib import pyplot as plt
# from datetime import datetime
import pandas as pd

# É necessário fazer o import de dates para trabalhar com formatação de datas na legenda do gráfico
# from matplotlib import dates as mpl_dates

plt.style.use('seaborn-v0_8-dark')


# dates = [
#     datetime(2019, 5, 24),
#     datetime(2019, 5, 25),
#     datetime(2019, 5, 26),
#     datetime(2019, 5, 27),
#     datetime(2019, 5, 28),
#     datetime(2019, 5, 29),
#     datetime(2019, 5, 30)
# ]

# y = [0, 1, 3, 4, 6, 5, 7]

# # Por padrão este tipo de plot possui apenas os pontos. Para adicionar uma linha basta passar algum argumento
# # em linestyle
# plt.plot_date(dates, y, linestyle='solid')

# # o método gfc significa get current figure, ele serve para selecionar e trabalhar diretamente na figura no lugar dos pontos.
# # o método autofmt_xdate serve para formatar a legenda das datas que estão no eixo x, inclinando para não se sobreporem
# plt.gcf().autofmt_xdate()

# # Usando o DateFormatter e incluindo ele como argumento de formato do eixo X, todos os itens serão formatados como
# # solicitado
# date_format = mpl_dates.DateFormatter('%b, %d %Y')
# plt.gca().xaxis.set_major_formatter(date_format)

df = pd.read_csv(r"Python/Matplotlib/time_series/data.csv")

# É necessário transformar datas em datetimes. Caso contrário, o matplotlib tratará as datas como strings
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True)

datas = df['Date']
valor = df["Close"]

plt.plot_date(datas, valor, linestyle="solid")

plt.gcf().autofmt_xdate()

plt.title('Valores do BitCoin')
plt.ylabel('Valor')
plt.grid(True)
plt.tight_layout()
plt.savefig(r"Python/Matplotlib/time_series/simple_time_series.png")
plt.show()

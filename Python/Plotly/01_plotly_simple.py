import plotly.express as px
from random import randrange

data_x = list(range(2015,2026))
data_y = [randrange(0,500) for i in range(11)]

fig = px.line(x=data_x, y=data_y, title=f'Dados aleatórios entre {data_x[0]} e {data_x[-1]}',line_shape='hv')

fig.show()
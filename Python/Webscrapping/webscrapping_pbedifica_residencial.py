import pandas as pd 
import requests
from bs4 import BeautifulSoup
path = r'Python/Webscrapping/'

tipo = "comercial"

link = 'https://pbeedifica.com.br/edificacoes-etiquetadas/residencial'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0'}

req = requests.get(link, headers=headers)

html = BeautifulSoup(req.text, 'html.parser')

divs_col = html.find_all('div', class_='col')

lista_nomes = []
lista_cidades = []
lista_estados = []
lista_datas = []

for div in divs_col:
    p = div.find('p')
    strong = p.find('strong')
    title = strong.get_text().replace('\u2013', '')
    if '/' in title:
        title = title.split('(')
        nome = title[0]
        data = title[1].replace(')', '').replace("Etiqueta de projeto", '').replace("Etiqueta da edificação construída", '').replace('-', '').replace("Etiquetade projeto", '').strip()
        lista_nomes.append(nome)
        lista_datas.append(data)
    else:
        lista_nomes.append(title)
        lista_datas.append(None)

    p = p.get_text().split('\n')[1].strip()
    if len(p) <= 50:
        local = p.replace('(', '').replace(")", '').replace("Localizada", '').replace("em", '').replace("no", '').strip()
        if len(local.split('/')) == 2:
            div_local = local.split('/')
            cidade = div_local[0]
            estado = div_local[1]
            lista_cidades.append(cidade)
            lista_estados.append(estado)
        elif len(local.split('-')) == 2:
            div_local = local.split('-')
            cidade = div_local[0]
            estado = div_local[1]
            lista_cidades.append(cidade)
            lista_estados.append(estado)
        elif len(local.split(', ')) == 2:
            div_local = local.split(', ')
            cidade = div_local[0]
            estado = div_local[1]
            lista_cidades.append(cidade)
            lista_estados.append(estado)
        else:
            lista_cidades.append(local)
            lista_estados.append(None)
    else:
        lista_cidades.append(p)
        lista_estados.append(None)

df = pd.DataFrame({
    'Edificação': lista_nomes,
    'Data': lista_datas,
    'Cidade': lista_cidades,
    'Estado': lista_estados
})

print(df)

df.to_csv(f'{path}edificacoes_residenciais_etiquetadas.csv', sep=';', index=False, encoding='latin-1')

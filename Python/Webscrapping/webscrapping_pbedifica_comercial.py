import pandas as pd 
import requests
from bs4 import BeautifulSoup
path = r'Python/Webscrapping/'

tipo = "comercial"

link = 'https://pbeedifica.com.br/edificacoes-etiquetadas/comercial'
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
    nome = strong.get_text().replace('\u2013', '')
    lista_nomes.append(nome)        

    p = p.get_text().split('\n')

    local_div = p[1].strip().split(", ")
    if len(local_div) == 1:
        local_div = p[1].strip().split("/")
    
    cidade = local_div[0]
    lista_cidades.append(cidade)
    estado = local_div[1]
    lista_estados.append(estado)

    data = p[2].strip()
    lista_datas.append(data)


df = pd.DataFrame({
    'Edificação': lista_nomes,
    'Data': lista_datas,
    'Cidade': lista_cidades,
    'Estado': lista_estados
})

print(df)

df.to_csv(f'{path}edificacoes_comerciais_etiquetadas.csv', sep=';', index=False, encoding='latin-1')

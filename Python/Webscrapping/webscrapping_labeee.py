import pandas as pd 
import requests
from bs4 import BeautifulSoup
path = r'GeneralPython/API&Pandas/'

link = 'https://labeee.ufsc.br/pt-br/sobre/pesquisadores'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0'}

req = requests.get(link, headers=headers)

html = BeautifulSoup(req.text, 'html.parser')

csv_name = html.find('title').get_text().split(' ')[0]

div = html.find('div', class_='node__content')

pesquisadores = div.findAll('td', attrs={'style': 'width: 220px;'})

lista_nomes = []
lista_lattes = []
lista_orcid = []
lista_researchgate = []

for item in pesquisadores: 
    pesquisador = item.get_text().split('\n')[0]
    lista_nomes.append(pesquisador)
    links = item.findAll('a')
    for i in links:
        rede = i.get_text()
        ref = i['href']
        match rede:
            case 'Orcid':
                lista_orcid.append(ref)
            case 'ResearchGate':
                lista_researchgate.append(ref)
            case 'Lattes':
                lista_lattes.append(ref)


df = pd.DataFrame()
df.loc[:, 'Nome'] = lista_nomes
df.loc[:, 'Lattes'] = lista_lattes
df.loc[:, 'Orcid'] = lista_orcid
df.loc[:, 'ResearchGate'] = lista_researchgate

print(df)

df.to_csv(f'{path}{csv_name}.csv', sep=';')

import pandas as pd
from datetime import date

path_citydata = 'csv_files'

# read csv
uf_line = pd.read_csv(path_citydata + '/city_data.csv')

# Data format = TMY_UF_etc_etc.csv

arquive = 'TMY_TO_teste.csv'

arquive = arquive.split("_")[1]

regions = []
counter = -1
for i in uf_line['region']:
    counter +=1
    regions.append({i: counter})

region_location = 0

uf = filename.split('_')[1]
uf_line = city_data.loc[city_data.region == uf:]

for i in regions:
    if arquive[1] == i.key():
        region_location = i.value()


# extracting info about the city
date_today = date.today()
city = uf_line.iloc[0]['city']
region = uf_line.iloc[0]['region']
country = uf_line.iloc[0]['country']
lat = uf_line.iloc[0]['lat']
lon = uf_line.iloc[0]['lon']
tz = uf_line.iloc[0]['tz']
alt = uf_line.iloc[0]['alt']
# city = df_city.loc()
# region = df_city.loc()
# country = df_city.loc()
# lat = df_city.loc()
# lon = df_city.loc()
# tz = df_city.loc()
# alt = df_city.loc()

result = {'city': city, 'region': region, 'country': country, 'lat': lat, 'lon': lon, 'tz': tz, 'alt': alt}

print(result)



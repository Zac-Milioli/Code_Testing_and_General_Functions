import pandas as pd

df = pd.read_csv('city_data_for_test.csv')

string1 = 'Acre'
string2 = 'TO'

df = df[~df.apply(lambda row: row.astype(str).str.contains(string1).any(), axis=1)]
df = df[~df.apply(lambda row: row.astype(str).str.contains(string2).any(), axis=1)]

print(df)

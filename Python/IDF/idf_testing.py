from eppy import modeleditor
from eppy.modeleditor import IDF

path_idf = r'GeneralPython/IDF/U001_Caso01_1a7_hi_in1.idf'
path_idd = r'GeneralPython/IDF/Energy+.idd'

IDF.setiddname(path_idd)

idf_file = IDF(path_idf)

nome = idf_file.idfobjects['building'][0].Name
print(nome)

termo_de_busca = idf_file.idfobjects['BUILDINGSURFACE:DETAILED']

zonas = []
for detalhe in termo_de_busca:
    if detalhe.Zone_Name not in zonas:
        print(detalhe.Zone_Name)
        zonas.append(detalhe.Zone_Name)

import pandas as pd


with open('BRA_AC_Rio.Branco-Medici.Intl.AP.829170_TMYx.2007-2021.epw', "r+") as f:
    d = f.readlines()
    f.seek(0)
    for i in d:
        if i not in [0, 1, 2, 3, 4, 5, 6, 7]:
            f.write(i)
    f.truncate()

print()

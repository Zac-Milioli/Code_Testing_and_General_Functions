import os

epw_name = open('exemplo.lst', "a")
text = 'TMY_2025-def-CST.cst'
text = 'TMY_2025-def-CST.cst\t'+(text.split('-'))[0]+'.epw\tNA\n'

epw_name.write(text)
epw_name.close()


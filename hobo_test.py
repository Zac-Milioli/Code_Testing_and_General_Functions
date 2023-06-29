import requests
import json

testing = requests.get('http://webservice-dev.hobolink.com/restv2/public/devices/1216485/data_files/latest/txt')

for i in testing:
    print(f'--{i}/n')

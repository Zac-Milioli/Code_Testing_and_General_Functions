import requests

testing = requests.get('http://webservice-dev.hobolink.com/restv2/public/devices/1216485/data_files/latest/txt')

print(testing)

for i in testing:
    print(f'-->{i}/n')

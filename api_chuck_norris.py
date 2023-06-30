import requests

url = 'https://api.chucknorris.io/jokes/random'

body = requests.get(url)

body = body.json()

print(body["value"])

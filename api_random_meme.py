import requests
from random import randrange
from io import BytesIO
from PIL import Image


url = 'https://api.imgflip.com/get_memes'

request = requests.get(url)

meme_url = (request.json())['data']['memes'][randrange(0, 99)]['url']

print(meme_url)

new_request = requests.get(meme_url)

Image.open(BytesIO(new_request.content)).show()

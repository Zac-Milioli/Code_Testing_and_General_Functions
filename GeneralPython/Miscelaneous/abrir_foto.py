# Teste simples de Pillow para abrir imagem

from PIL import Image

path = 'hacker.jfif'

imagem = Image.open(path)

imagem.show()

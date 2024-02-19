from pdf2image import convert_from_path
from PIL import Image


pdf = convert_from_path('.pdf')

imagem = Image.open(pdf)

imagem.save('.png', 'PNG')

import requests
from PIL import Image
from io import BytesIO

# Faz a chamada na API HTTP Dogs
response = requests.get("https://http.dog/[200].jpg")

# Verifica se a resposta possui o status 200 (OK)
if response.status_code == 200:
    # Extrai o conteúdo da imagem da resposta
    image_data = response.content

    # Cria um objeto de imagem a partir dos dados retornados
    image = Image.open(BytesIO(image_data))

    # Exibe a imagem no terminal
    image.show()
else:
    print("Erro na requisição. Status:", response.status_code)

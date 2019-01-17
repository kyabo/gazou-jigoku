import sys
from PIL import Image, ImageDraw

# Endereco da imagem
imagem = sys.argv[1]

# Abre a imagem original em modo tons de cinza
origem = Image.open(imagem).convert('L')

# Cria a imagem de destino
destino = Image.new('L', (origem.width, origem.height))
destinoDraw = ImageDraw.Draw(destino)

# NEGATIVO
for x in range(origem.width):
    for y in range(origem.height):
        destinoDraw.point((x, y), (255-origem.getpixel((x, y))))

# Salva a imagem
destino.save('negativo_' + imagem)

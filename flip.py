import sys
from PIL import Image, ImageDraw

# Endereco da imagem
imagem = sys.argv[1]

# Abre a imagem original em modo tons de cinza
origem = Image.open(imagem).convert('L')

# Cria a imagem de destino
destino = Image.new('L', (origem.width, origem.height))
destinoDraw = ImageDraw.Draw(destino)

# FLIP
origw = origem.width
for x in range(origw):
    for y in range(origem.height):
        destinoDraw.point((x, y), origem.getpixel(((origw-x)-1, y)))

# Salva a imagem
destino.save('flip_' + imagem)

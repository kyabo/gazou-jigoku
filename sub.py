import sys
from os import path
from PIL import Image, ImageDraw

# Endereco das imagens
imagemA = sys.argv[1]
imagemB = sys.argv[2]

# Abre as imagens originais em modo tons de cinza
origemA = Image.open(imagemA).convert('L')
origemB = Image.open(imagemB).convert('L')

# Cria a imagem de destino
destino = Image.new('L', (origemA.width, origemA.height))
destinoDraw = ImageDraw.Draw(destino)

# subtração
for x in range(origemA.width):
    for y in range(origemA.height):
        destinoDraw.point((x, y), (origemA.getpixel((x, y)) - origemB.getpixel((x, y))))

# Salva a imagem
nomeA, ext = path.splitext(imagemA)
nomeB = path.splitext(imagemB)[0]
destino.save(nomeA + ' - ' + nomeB + ext)

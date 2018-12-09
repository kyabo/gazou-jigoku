import sys
from PIL import Image

# Endereco da imagem
imagem = sys.argv[1]

# Abre a imagem original em modo tons de cinza
origem = Image.open(imagem).convert('L')

# Cria a imagem de destino
destino = Image.new('L', (origem.width*2, origem.height*2))

# Nearest Neighbor para ampliação
destx = 0
desty = 0
for x in range(origem.width):
    for y in range(origem.height):
        pixel = origem.getpixel((x, y))
        destino.putpixel((destx, desty), pixel)
        destino.putpixel((destx+1, desty), pixel)
        destino.putpixel((destx, desty+1), pixel)
        destino.putpixel((destx+1, desty+1), pixel)
        desty += 2
    destx += 2
    desty = 0

# Salva a imagem
destino.save('NNamp_' + imagem)

import sys
from PIL import Image

# Endereco da imagem
imagem = sys.argv[1]

# Abre a imagem original em modo tons de cinza
origem = Image.open(imagem).convert('L')

# Cria a imagem de destino
destino = Image.new('L', (int(origem.width*0.5), int(origem.height*0.5)))

# Bilinear para redução
origx = 0
origy = 0
for x in range(destino.width):
    for y in range(destino.height):
        pixel1 = origem.getpixel((origx, origy))
        pixel2 = origem.getpixel((origx+1, origy))
        pixel3 = origem.getpixel((origx, origy+1))
        pixel4 = origem.getpixel((origx+1, origy+1))
        _pixel = int((pixel1+pixel2+pixel3+pixel4)/4)
        destino.putpixel((x,y),_pixel)
        origy += 2
    origx += 2
    origy = 0

# Salva a imagem
destino.save('Bilinearred_' + imagem)

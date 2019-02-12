import sys
from PIL import Image, ImageDraw

# Endereco da imagem
imagem = sys.argv[1]

# Abre a imagem original em modo tons de cinza
origem = Image.open(imagem).convert('L')

# Cria a imagem de destino
destino = Image.new('L', (origem.width, origem.height))
destinoDraw = ImageDraw.Draw(destino)

# Cria a mascara
mask = [[1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]]

# Divisor Constante
div = 9

# Magias
for x in range(origem.width):
    for y in range(origem.height):

        # Variaveis auxiliares para a soma (e o padding com zeros)
        z1 = 0
        z2 = 0
        z3 = 0
        z4 = 0
        z5 = mask[1][1]*origem.getpixel((x, y))
        z6 = 0
        z7 = 0
        z8 = 0
        z9 = 0
        
        if x > 0 and y > 0:
            z1 = mask[0][0]*origem.getpixel((x-1, y-1))
                       
        # Checando limites inferiores...    
        if x > 0:
            z4 = mask[0][1]*origem.getpixel((x-1, y))
            if y < origem.height-1:
                z7 = mask[0][2]*origem.getpixel((x-1, y+1))
            
        if y > 0:
            z2 = mask[1][0]*origem.getpixel((x, y-1))
            if x < origem.width-1:
                z3 = mask[2][0]*origem.getpixel((x+1, y-1))

        # Checando limites superiores...
        if x < origem.width-1 and y < origem.height-1:
            z9 = mask[2][2]*origem.getpixel((x+1, y+1))
        
        if x < origem.width-1:
            z6 = mask[2][1]*origem.getpixel((x+1, y))

        if y < origem.height-1:
            z8 = mask[1][2]*origem.getpixel((x, y+1))

        # Adiciona a média dos pixels ao destino
        destinoDraw.point((x, y), (int)((z1+z2+z3+z4+z5+z6+z7+z8+z9)/div))
            
# Salva a imagem
destino.save('media_' + imagem)

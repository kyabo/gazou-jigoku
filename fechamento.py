import sys
from PIL import Image, ImageDraw

# Endereco da imagem
imagem = sys.argv[1]

# Abre a imagem original em modo tons de cinza e binariza
origem = Image.open(imagem).convert('L').point(lambda c: c > 127 and 255)


# Cria uma imagem auxiliar
mid = Image.new('L', (origem.width, origem.height))
midDraw = ImageDraw.Draw(mid)

# Cria a imagem de destino
destino = Image.new('L', (origem.width, origem.height))
destinoDraw = ImageDraw.Draw(destino)

# Elemento estruturante
mask = [[0, 255, 0],
        [255, 255, 255],
        [0, 255, 0]]

# Dilatacao
for x in range(origem.width):
	for y in range(origem.height):
		pixel = origem.getpixel((x,y))
		if pixel == mask[1][1]:
			if y > 0:
				if mask[0][0] == 255 and x > 0:
					midDraw.point((x-1, y-1), 255)
				if mask[1][0] == 255:
					midDraw.point((x, y-1), 255)
				if mask[2][0] == 255 and x < origem.width - 1:
					midDraw.point((x+1, y-1), 255)

			if mask[0][1] == 255 and x > 0:
				midDraw.point((x-1, y), 255)
			# ponto do meio:
			midDraw.point((x, y), 255)
			if mask[2][1] == 255 and x < (origem.width - 1):
				midDraw.point((x+1, y), 255)

			if y < origem.height - 1:		
				if mask[0][2] == 255 and x > 0:
					midDraw.point((x-1, y+1), 255)
				if mask[1][2] == 255:
					midDraw.point((x, y+1), 255)
				if mask[2][2] == 255 and x < (origem.width - 1):
					midDraw.point((x+1, y+1), 255)

# Erosao
er = true

for x in range(mid.width):
	for y in range(mid.height):
		if mask[0][0] != 0:
			if x > 0 and y > 0:
				if mask[0][0] != mid.getpixel((x-1, y-1)):
					er = false
			else:
				er = false

		if mask[1][0] != 0:
			if y > 0:
				if mask[1][0] != mid.getpixel((x, y-1)):
					er = false
			else:
				er = false

		if mask[2][0] != 0:
			if y > 0 and x < mid.width - 1:
				if mask[2][0] != mid.getpixel((x+1, y-1)):
					er = false
			else:
				er = false
		
		if mask[0][1] != 0:
			if x > 0:
				if mask[0][1] != mid.getpixel((x-1, y)):
					er = false
			else:
				er = false

		if mask[1][1] != 0:
			if mask[1][1] != mid.getpixel((x, y)):
					er = false

		if mask[2][1] != 0:
			if x < mid.width - 1:
				if mask[2][1] != mid.getpixel((x+1, y)):
					er = false
			else:
				er = false

		if mask[0][2] != 0:
			if y < mid.height - 1 and x > 0:
				if mask[0][2] != mid.getpixel((x-1, y+1)):
					er = false
			else:
				er = false

		if mask[1][2] != 0:
			if y < mid.height - 1:
				if mask[1][2] != mid.getpixel((x, y+1)):
					er = false
			else:
				er = false

		if mask[2][2] != 0:
			if y < mid.height - 1 and x < mid.width - 1:
				if mask[2][2] != mid.getpixel((x+1, y+1)):
					er = false
			else:
				er = false

		# finalmente, adicionar o pixel ao destino
		if er == true:
			destinoDraw.point((x, y), 255)

# Salva a imagem
destino.save('fechamento_' + imagem)

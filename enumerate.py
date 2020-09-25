lista = [18, 7, 20, 3, 9]
for index, value in enumerate(lista):
	if value == max(lista):
		print('o valor maximo, {}, esta na posicao {}'.format(value, index))
	if value ==min(lista):
		print('O valor minimo, {}, esta na posicao {}'.format(value, index))
pessoas = []
continuar = 's'
while continuar == 's':
    nome = input('qual o seu nome? ')
    peso = int(input('qual o seu peso? '))
    pessoas.append((nome, peso))
    continuar = input('quer continuar? ')
peso_max = 0
peso_min = 500
for pessoa in pessoas:
    if pessoa[1] > peso_max:
        peso_max = pessoa[1]
    if pessoa[1] < peso_min:
        peso_min = pessoa[1]
mais_pesadas = []
mais_leves = []
for pessoa in pessoas:
    if pessoa[1] == peso_max:
        mais_pesadas.append(pessoa[0])
    if pessoa[1] == peso_min:
        mais_leves.append(pessoa[0])
print('{} pessoas foram cadastradas'.format(len(pessoas)))
print('as pessoas mais pesadas com {}Kg sao {}'.format(peso_max, mais_pesadas))
print('as pessoas mais leves com {}Kg sao {}'.format(peso_min, mais_leves))

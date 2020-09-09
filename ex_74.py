import random

n1 = random.randint(0, 9)
n2 = random.randint(0, 9)
n3 = random.randint(0, 9)
n4 = random.randint(0, 9)
my_tuple = (n1, n2, n3, n4)
sorting = sorted(my_tuple)
print('o maior numero e: {}'.format(sorting[0]))
print('o menor numero e: {}'.format(sorting[-1]))


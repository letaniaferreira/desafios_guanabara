# import random
#
# n1 = random.randint(0, 9)
# n2 = random.randint(0, 9)
# n3 = random.randint(0, 9)
# n4 = random.randint(0, 9)
# my_tuple = (n1, n2, n3, n4)
# sorting = sorted(my_tuple)
# print('o maior numero e: {}'.format(sorting[0]))
# print('o menor numero e: {}'.format(sorting[-1]))

from random import sample
# num = tuple(sample(range(10),5))
# print(num)
# print('o maior valor e{}'.format(max(num)))
# print('o menor valor e{}'.format(min(num)))
print(sample(range(10),5))

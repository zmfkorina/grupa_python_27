import random
from lib.core import even_numbers, is_even

# print(random.sample(range(0, 1000), 15))

random_numbers = [609, 814, 455, 15, 196, 9, 993, 342, 398, 306, 779, 710, 38, 651, 90]

# filter(), map(), reduce(), zip()

# lambda functions:

def mult_2(param1):
    return param1 * 2


print(mult_2(10))

# efemera
square = lambda x: x * 2
print(square(10))

# filtrati toate numerele multiplu de 7 din random_numbers

rezultat = list(filter(lambda x: x % 13 == 0, random_numbers))
print(rezultat)

rezultat2 = list(filter(is_even, random_numbers))
print(rezultat2)
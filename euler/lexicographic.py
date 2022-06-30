# millionth lexicographic permutation of 0..9
from itertools import permutations

g = permutations("0123456789", 10)

for i in range(1, 1000000):
    next(g)

print("".join(next(g)))

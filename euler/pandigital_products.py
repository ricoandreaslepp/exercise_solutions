# 1..9 pandigital
# sum of all products, only once
# 1-4-4
# 2-3-4
from itertools import permutations

prods = set()

def solve():
    global prods
    
    g = permutations("123456789", 9)
    
    while True:
        try:
            s = "".join(next(g))
            
            if int(s[:2])*int(s[2:5]) == int(s[5:]):
                prods.add(int(s[5:]))
                
            if int(s[0])*int(s[1:5]) == int(s[5:]):
                prods.add(int(s[5:]))
                
        except StopIteration:
            return prods

print(sum(solve()))

# four non-trivial examples
# <1 in value
# 2 digits in numerator and denominator
from fractions import Fraction

s = set()

def solve():
    for i in range(10, 100):
        for j in range(i+1, 100):
            
            a, b = map(str, [i, j])
            for x in a:

                if x in b and x!='0':
                    # try removing
                    temp_a, temp_b = (str.replace(x, '') for str in [a, b])

                    if temp_a and temp_b and int(temp_b)!=0:

                        if int(temp_a)/int(temp_b) == i/j and i/j<1:
                            s.add(f"{i}/{j}=={temp_a}/{temp_b}")
    
    total = Fraction(1, 1)
    for i in s:
        total *= Fraction(int(i[:2]), int(i[3:5]))
        
    return total
    
if __name__ == "__main__":   
    print(solve())

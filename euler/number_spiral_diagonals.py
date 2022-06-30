# 1001 by 1001 spiral diagonals sum

# +2
# +4
# +6
# +8

# 1 + 3+5+7+9 + 13+17+21+25 + 31+37+43+49

# 3 + 3+2 + 3+4 + 3+6
# 13 + 13+4 + 13+8 + 13+12
# 31 + 31+6 + 31+12+ 31+18
from math import floor

n = int(input())
twos = 2
keep = 3
ans = 1
for i in range(floor(n/2)): # skip first layer
    
    for j in range(0, 4):
        ans += (keep + (j*twos))
    
    # incrementing
    keep += 4*twos+2
    twos += 2

print(ans)
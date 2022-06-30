# 2020/2021 lõppvoor 3. ül

# masina number
def uuri(n):
    global dp, masinad
    
    a = masinad[n-1]
    
    ostuhind = a[0]
    kogus = a[1]
    m = a[2:]
    m.sort(reverse=True)
    
    if kogus==0:
        dp[n] = ostuhind
        return ostuhind

    ehitades = 0
    for i in m:
        if dp[i] != None:
            ehitades += dp[i]
        else:
            ehitades += uuri(i)
    
    dp[n] = min(ehitades, ostuhind)
    return min(ehitades, ostuhind)

def solve(inp):
    global dp, masinad
    n, k = map(int, inp[0].split(" "))
    
    masinad = []
    for i in range(1, n+1):
        masinad.append(list(map(int, inp[i].split(" "))))
    
    dp = [None for _ in range(1, 1002)]
    return uuri(k)
        

# 2020/2021 lõppvoor 2. ül

def solve(inp):
    n, m = map(int, inp[0].split(" "))
    
    ahvid = []
    for i in range(1, n+1):
        ahvid.append(list(map(int, inp[i].split(" "))))
    
    ans = 0
    cnt = -200*100
    for i in range(n):
        hypped = ahvid[i]
        teadmata = -sum(hypped)
        
        k = 0
        pos = 0
        for h in hypped:
            if h == 0:
                pos += teadmata
            else:
                pos += h

            k += pos

        if k/m > cnt:
            cnt = k/m
            ans = i
            
    return ans+1

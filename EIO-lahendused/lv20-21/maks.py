def solve(inp):
    n = int(inp[0])
    a = list(map(int, inp[1].split(" ")))
    a.sort()
    
    acum = 0
    for i in a:
        if acum+1<i:
            break
        acum += i
        
    return acum+1

print(solve(["4", "1 2 3 4"]))
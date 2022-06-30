import sys
sys.setrecursionlimit(2000)

n, m = list(map(int, input().split(" ")))

laud = []
for _ in range(n):
    laud.append(list(input()))

def locate(n, m):
    for i in range(n):
        for j in range(m):
            if laud[i][j] == '#':
                return (i, j)

def printer(l):
    for rida in l:
        print("".join(rida))
        
# KUI MUUDAD RIDA SIIS MUUDA VEERGU EHK V
def veerg(r, v):
    if r+1 < n:
        if laud[r+1][v] == '.': laud[r+1][v] = '+'
    if r-1 >= 0:
        if laud[r-1][v] == '.': laud[r-1][v] = '+'
    
def rida(r, v):
    if v+1 < m:
        if laud[r][v+1] == '.': laud[r][v+1] = '+'   
    if v-1 >= 0:
        if laud[r][v-1] == '.': laud[r][v-1] = '+'

# ääred
def hupe_veerg(r, v):
    
    if r+2 < n:
        if laud[r+1][v] == '*' and laud[r+2][v] == '.':
            laud[r+2][v] = '+' # uus asukoht ja uuri edasi
            hupe_veerg(r+2, v)
            hupe_rida(r+2, v)
    
    if r-2 >= 0:
        if laud[r-1][v] == '*' and laud[r-2][v] == '.':
            laud[r-2][v] = '+' # uus asukoht ja uuri edasi
            hupe_veerg(r-2, v)
            hupe_rida(r-2, v)

    
def hupe_rida(r, v):
    
    if v+2 < m:
        if laud[r][v+1] == '*' and laud[r][v+2] == '.':
            laud[r][v+2] = '+' # uus asukoht ja uuri edasi
            hupe_veerg(r, v+2)
            hupe_rida(r, v+2)
    
    if v-2 >= 0:
        if laud[r][v-1] == '*' and laud[r][v-2] == '.':
            laud[r][v-2] = '+' # uus asukoht ja uuri edasi
            hupe_veerg(r, v-2)
            hupe_rida(r, v-2)


# ----------------
r, v = locate(n,m)
#printer(laud)
#print()

# hüpped
rida(r, v)
veerg(r, v)
hupe_rida(r, v)
hupe_veerg(r, v)
# ------
printer(laud)

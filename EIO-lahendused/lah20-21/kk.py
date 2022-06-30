n, s = map(int, input().split(" "))
hüpped = [list(map(int, input().split(" "))) for _ in range(s)]

def gcdExtended(a, b):
    if a == 0 :
        return b,0,1

    gcd,x1,y1 = gcdExtended(b%a, a)

    x = y1 - (b//a) * x1
    y = x1

    return gcd,x,y

aox = 1
b = 0
for i in range(s-1, -1, -1):
    b += (aox * (hüpped[i][0]-hüpped[i][1]))
    b = (b % n)

    aox *= hüpped[i][1]
    aox = (aox % n)

u, k = map(int, input().split(" "))

if k<0:
    k = abs(k)
    g, x, y = gcdExtended(aox, n)
    aox = x % n
    b = (-b*x) % n

if aox-1==0:
    u = (pow(aox, k, n)*u % n + (k*b)) % n # jada summa tuleb leida teistmoodi
else:
    u = (pow(aox, k, n)*u % n + (((pow(aox, k, n*(aox-1))-1)//(aox-1)) * b)) % n
   

if u==0:
    print(n)
else:
    print(u)

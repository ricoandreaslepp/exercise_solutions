vastused = []

def lisa_vastus(algus, lõpp):
    global vastused
    if algus==lõpp:
        vastused.append(f"{algus}")
    else:
        vastused.append(f"{algus}..{lõpp}")

K = int(input())
N = int(input())

# sorteerime ja eemaldame dubleeritud
a = sorted(set(map(int, [input() for i in range(N)])))

for i in range(len(a)+1):
    if i==0: # esimene
        if a[i]-K>0 and a[i]>1:
            lisa_vastus(a[i]-K, a[i]-1)
        elif a[i]>1:
            lisa_vastus(1, a[i]-1)
    elif i < len(a): # keskmised
        if not a[i-1]+1==a[i]:
            if a[i-1]+K+1 >= a[i]-K: # K-d overlapivad
                lisa_vastus(a[i-1]+1, a[i]-1)
            else:
                lisa_vastus(a[i-1]+1, a[i-1]+K)
                lisa_vastus(a[i]-K, a[i]-1)
    else: # viimane
	    lisa_vastus(a[i-1]+1, a[i-1]+K)

for line in vastused:
    print(line)
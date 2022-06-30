n, m = map(int, input("").split(" "))
lahendatud = list(map(int, input("").split(" ")))
küsimused = list(map(int, input("").split(" ")))

# max 1.1s
# ------------------------------- 
kõik_summad = set()
for i in range(0, n):
    for j in range(i+1, n+1):
        kõik_summad.add(sum(lahendatud[i:j]))

kõik_summad = set(sorted(kõik_summad))
# --------------------------------

# max 0.2s
# --------------------------------
kokku = sum(lahendatud)

for küs in küsimused: 
        
    if küs > kokku: 
        print("EI")
        pass
    else: 
        
        if küs in kõik_summad: # pole oluline, mis indeksil see on
            print("JAH")
            pass
        else:
            print("EI")
# --------------------------------

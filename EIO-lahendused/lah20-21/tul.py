n = int(input(""))

tulemused = {}
for _ in range(n):
    sis = input("").split(" ")
    nimi = sis[0]
    harjutus = sis[1]
    tulemus = int(sis[2])
    
    # kui nimi on olemas
    if nimi in tulemused.keys():
        
        # kui harjutus on olemas
        if harjutus in tulemused[nimi]:
            
            # kui tulemus on suurem 
            if tulemused[nimi][harjutus] < tulemus:
                tulemused[nimi][harjutus] = tulemus
        
        # kui harjutust pole olemas
        else:
            tulemused[nimi][harjutus] = tulemus
    # kui nime pole
    else:
        
        tulemused[nimi] = {harjutus : tulemus}
        
lõpptulemused = {}
for osaleja in tulemused:
    lõpptulemused[osaleja] = sum(tulemused[osaleja].values())

lõpptulemused = {k: v for k, v in sorted(lõpptulemused.items(), key=lambda item: item[1], reverse=True)}

for tulemus in lõpptulemused:
    print(tulemus, lõpptulemused[tulemus])
    

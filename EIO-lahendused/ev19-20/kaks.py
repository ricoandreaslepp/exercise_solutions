sonum = ["E"]
s = input().split(" ")[1:-1]
for arv in s:
    
    nullid = None
    # leiame pikima nullide jada
    # kõik nullide jadad, mis on pikemad kui 2
    while "000" in arv:
        for i in range(256, 2, -1):
            if "0"*i in arv:
                nullid = i
                break

        # leidis nulle
        if nullid:

            if nullid>15:
                arv = arv.replace("0"*nullid, f"B0{hex(nullid)[2:].upper()}")
            elif 15>=nullid>=3:
                arv = arv.replace("0"*nullid, f"B{hex(nullid)[2:].upper()}")

    if len(arv)<=15:
        lisada = f"A{hex(len(arv))[2:].upper()}{arv}"
    else:
        lisada = f"A0{hex(len(arv))[2:].upper()}{arv}"
    
    sonum.append(lisada)

sonum.append("F")
sonum.append("D") if len("".join(sonum))%2 else None
print("".join(sonum))

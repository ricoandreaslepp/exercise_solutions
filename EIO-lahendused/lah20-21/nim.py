n = int(input(""))

nimed = {}
for i in range(n):
    sis = input("").split(" ")
    nimed[sis[0]] = sis[1]

for i in range(n):
    sis = input("").split(" ")
    print(nimed[sis[0]] + " " + sis[1])
    

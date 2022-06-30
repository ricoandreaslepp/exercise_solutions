from string import ascii_lowercase

def tee_käigud(täht, arv):
	v = []
	v.append([täht-1, arv+2])
	v.append([täht+1, arv+2])
	v.append([täht-1, arv-2])
	v.append([täht+1, arv-2])
	v.append([täht+2, arv-1])
	v.append([täht+2, arv+1])
	v.append([täht-2, arv-1])
	v.append([täht-2, arv+1])

	t = set()
	for täht, arv in v:
		if täht in range(8) and arv in range(1, 9):
			t.add(f"{ascii_lowercase[täht]}{arv}")

	return t

täht, arv = input()
täht = ord(täht)-ord('a')
arv = int(arv)

käigud = set()
# peale teist käiku
for koht in tee_käigud(täht, arv):
	käigud = käigud.union(tee_käigud(ord(koht[0])-ord('a'), int(koht[1])))

for i in sorted(list(käigud)):
	print(i)


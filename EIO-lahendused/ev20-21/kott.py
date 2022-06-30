def vahetus(nimekiri, summa, hinnad, kingid, alg, lopp):
	i = nimekiri[alg]
	j = nimekiri[lopp]
	vana = kingid[i]*hinnad[i] + kingid[j]*hinnad[j]
	uus = kingid[i]*hinnad[j] + kingid[j]*hinnad[i]
	return summa-(vana-uus)

def solve(inp):
	# võib kaks hinda omavahel ära vahetada
	# leia selline vahetus, et kuluv summa oleks vähim
	n = int(inp[0])
	hinnad = {}
	for i in range(1, 2*n+1, 2):
		hinnad[inp[i]] = int(inp[i+1])
	nimekiri = list(hinnad)

	kingid = {}
	for item in hinnad.keys():
		kingid[item] = 0
	for i in range(2*n+2, 2*n+2+int(inp[2*n+1])):
		kingid[inp[i]] += 1

	summa = 0
	for kink in kingid.keys():
		summa += kingid[kink]*hinnad[kink]
	ans = summa
	#print(summa)

	# vahetused
	# ------------------------------------------
	for i in range(n):
		for j in range(i+1, n):
			uus = vahetus(nimekiri, summa, hinnad, kingid, i, j)
			#print(uus)
			ans = min(ans, uus)

	return ans

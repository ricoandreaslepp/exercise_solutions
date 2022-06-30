suurim = 0
n, m = map(int, input().split(" "))
adal = n+10*m

for _ in range(5):
	n, m = map(int, input().split(" "))
	suurim = max(suurim, n+10*m)

if suurim >= adal:
	print(suurim-adal+1)
else:
	print(0)

# lõpus võib olla ükskõik kui pikk jupp
n = int(input())
p = list(map(int, input().split(" ")))
#print(n, p)

for i in range(p[0]):
	l = i
	r = p[0] - l
	for j in range(1, n-1):
		l = r
		r = p[j] - l

		if r > p[j+1]:
			print("EI")
			sys.exit(0)

ans = [0]
for i in range(1, n-1):
	ans.append(p[i]*2)
print(" ".join(map(str, ans)))

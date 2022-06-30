mängijate_numbrid = list(map(int, input().split()))
mängude_võitjad = list(map(int, input().split()))

võitja = None
pool_finaal = [None for _ in range(4)]
finaal = [None for _ in range(2)]

c = {0:0, 1:0, 2:1, 3:1, 4:2, 5:2, 6:3, 7:3}
for võit in mängude_võitjad:

	if võit not in pool_finaal: # juba teame
		koht = mängijate_numbrid.index(võit)
		pool_finaal[c[koht]] = võit

	elif võit not in finaal: # tegeleme finaaliga
		koht = pool_finaal.index(võit)
		finaal[c[koht]] = võit
	else:
		võitja = võit

print(
f"""{võitja}
{' '.join(map(str, finaal))}
{' '.join(map(str, pool_finaal))}""")

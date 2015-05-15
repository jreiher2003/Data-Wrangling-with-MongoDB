nba_team = ['chi','tor','cle','ny','nj','det']
nba = list(enumerate(nba_team, start=1))
print nba
print nba[0][0]


def enumerate(lst, start=1):
	n = start
	for elem in lst:
		yield n, elem
		n +=1

print list(enumerate(nba_team, start=1))
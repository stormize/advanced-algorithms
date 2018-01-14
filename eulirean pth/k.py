#Uses python3
from collections import defaultdict
binary= int(input())
lpos = binary-1
last_binary ='1'*binary
_int = int(last_binary, 2)
last_before = "1"+('0'*lpos)
first = '0'*binary
nodes = defaultdict(list)
for i in range(0,_int+1):
		a = (bin(i)[2:].zfill(binary))
		if (a!=last_before and a!=first):
			s = a[0:lpos]
			e = a[1:binary]
			nodes[s].append(e)
			nodes[e].append(s)
start = '0'*(binary-1)
tour = [start]
cur = start
while(len(nodes[cur])>0):
	suf = cur[1:]
	nextChar = "1" if suf+"1" in nodes[cur] else "0"
	tour.append(suf+nextChar)
	nodes[cur].remove(suf+nextChar)
	nodes[suf+nextChar].remove(cur)
	cur = suf+nextChar
ou_res ='0'
for i,d in enumerate(tour):
   ou_res+=d[0]

print(ou_res)
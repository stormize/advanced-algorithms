#Uses python3

data = input().split()
n = int(data[0])
m = int(data[1])
ea = []
for i in range(m):
    ea.append(list(map(int, input().split())))

ad= [[] for _ in range(n)]
n = 0
for (a, b) in ea:
    ad[a - 1].append(((b - 1), n))
    n += 1


d = [0]*n
for s, e in ea:
    d[s-1]+=1
    d[e-1]-=1
if any(d):
    print(0)
else:
    p = [0]
    vi = set()
    while len(vi)<len(ea):
        for i, po in enumerate(p):
            allVisited = True
            for nextPoint in ad[po]:
                if nextPoint[1] not in vi:
                    allVisited = False
                    break
            if allVisited: continue
            new_cycle = [po]
            cur = po
            findNext = True
            while findNext:
                findNext = False
                for nextPoint in ad[cur]:
                    if nextPoint[1] not in vi:
                        vi.add(nextPoint[1])
                        new_cycle.append(nextPoint[0])
                        cur = nextPoint[0]
                        findNext = True
                        break
            break
        p = p[:i]+new_cycle+p[i+1:]
    p = list(map(lambda x: str(x+1), p))[:-1]
    print(1)
    print(" ".join(p))

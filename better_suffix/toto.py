#python 3
from itertools import permutations
def overlap(str1,str2,min):
    start=0
    while True:
        start = str1.find(str2[:min],start)
        if start==-1:
            return 0
        if str2.startswith(str1[start:]):
            return  len(str1)-start
        start+=1
def max_overlap(reads,k):
    a,b=None,None
    best=0
    for i,j in permutations(reads,k):
        olap=overlap(i,j,k)
        if olap >best:
            a,b=i,j
            best=olap
    return a,b,best
def greedy(reads,k):
    reada,readb,olen=max_overlap(reads,k)
    while olen>0:
        reads.remove(reada)
        reads.remove(readb)
        reads.append(reada+readb[olen:])
        reada, readb, olen = max_overlap(reads, k)
    return ''.join(reads)
reads = []
for _ in range(1618):
    reads.append(input())
print(greedy(reads,2))
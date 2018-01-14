#python 3
import sys


def optimal(km,reads):
 k = set ()
 for r in reads:
     for i in range(0,len(r)-km+1):
         k.add(r[i:i+km])
 p =set()
 s=set()
 for kmer in k:
     p.add(kmer[:-1])
     s.add(kmer[1:])
 return p==s
reads=[]
for _ in range(1618):
    r = sys.stdin.readline().strip()
    reads.append(r)
for k in range(len(reads[2]),1,-1):
     if optimal(k,reads):
         print(k)
         break


#python 3
def gauss(m):
    n=len(m)
    for i in range(n):
        pivot(i,n,m)
        for j in range(i+1,n):
            m[j]=[m[j][k]-m[i][k]*m[j][i]/m[i][i] for k in range(n+1)]
    if m[n - 1][n - 1] == 0: raise ValueError('No unique solution')

    x = [0] * n
    for i in range(n - 1, -1, -1):
        s = sum(m[i][j] * x[j] for j in range(i, n))
        x[i] = (m[i][n] - s) / m[i][i]
    return x

def pivot(i,n,m):
    max=-1e100
    for j in range(i,n):
        if max <abs(m[j][i]):
            max_row,max=j,abs(m[j][i])
    m[i],m[max_row]=m[max_row],m[i]

n = input().split(" ")
m=[]
if n >0:
 for i in range(0,n):
    eq=[]
    aq=input().split(" ")
    for i in aq:
        eq . append(float(i))
    m.append(eq)
 for j in gauss(m):
     print(j)

def create_table(a,b,c):

    tableau = [row[:]+[x] for row, x in zip(a, b)]
    tableau.append([ci for ci in c] + [0])
    print(tableau)
    return tableau

def find_col(table):
    max=999999999
    col=-1
    for i in range (0,len(table[-1])):
        if max>table[-1][i]:
            max =table[-1][i]
            col=i
    return  col
def find_row(table):
    col=find_col(table)
    min =float("inf")
    row =-1
    for i in range(0,len(table)):
       if not i ==len(table)-1:
        if not table[i][col]==0:
          if min >table[i][len(table[-1])-1]/table[i][col]:
              min=table[i][len(table[-1])-1]/table[i][col]
              row=i
    return row

def pivot_row(table):
    col=find_col(table)
    row=find_row(table)
    number=table[row][col]
    for i in range(0,len(table[-1])):
        table[row][i]/=number
    print(table)
    return col,row

def other_row(table):
    pivot_info=pivot_row(table)
    print(pivot_info)
    for i in range(0,len(table)):
        r = table[i][pivot_info[0]]
        for j in range(0,len(table[-1])):
            if not i ==pivot_info[1]:

             table[i][j]=table[i][j]-(r*table[pivot_info[1]][j])
    return table

def canImprove(tableau):
   lastRow = tableau[-1]
   return any(x < 0 for x in lastRow[:-1])



















n=input()
m = [int(tkn) for tkn in n.split()]
A,B,C=[],[],[]
for i in range(0,m[0]):
    adds = []
    temp=input()
    a= [int(tkn) for tkn in temp.split()]
    for j in range (0,m[0]+1):
        adds.append(0)
    adds[((i+4)-(m[0]+1))%(m[0]+1)]=1
    a=a+adds
    A.append(a)

b=input()
B=[float(tkn) for tkn in b.split()]
c=input()
C=[float(tkn) for tkn in c.split()]
for i in range(0,m[0]):
    C.append(0)
C.append(1)
table =create_table(A,B,C)
while(canImprove(table)):
 table =other_row(table)
 print(table)
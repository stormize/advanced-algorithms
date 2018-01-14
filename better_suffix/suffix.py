#python 3

def char_sort(string):
    count=[0]*122
    order=['%']*(len(string))
    for i in range(0,len(string)):
        count[ord(string[i])]=count[ord(string[i])]+1
    for i in range(1,122):
        count[i]=count[i]+count[i-1]
    for i in range(len(string)-1,-1,-1):
        c=ord(string[i])
        count[c]=count[c]-1
        order[count[c]]=i
    return order
def classes(string,order):
    myclass=[0]*len(string)
    myclass[order[0]]=0
    for i in range(1,len(string)):
        if not string[order[i]]==string[order[i-1]]:

            myclass[order[i]]=myclass[order[i-1]]+1
        else:

            myclass[order[i]]=myclass[order[i-1]]
    return myclass

def sort_doubled(l,myclass,string,order):
    count =[0]*len(string)
    new_order=[0]*len(string)
    for i in range(0,len(string)):
        count[myclass[i]]=count[myclass[i]]+1
    for i in range(1,len(string)):
        count[i]=count[i]+count[i-1]
    for i in range(len(string)-1,-1,-1):
        start=(order[i]-l+len(string))%len(string)
        c=myclass[start]
        count[c]=count[c]-1
        new_order[count[c]]=start
    return new_order
def update_class(new_order,myclass,l):
    n=len(new_order)
    new_class=[0]*n
    new_class[new_order[0]]=0
    for i in range(1,n):
        cur=new_order[i]
        prev=new_order[i-1]
        mid=(cur+l) %n
        mid_prev=(prev+l) %n

        if not myclass[cur]==myclass[prev] or not myclass[mid]==myclass[mid_prev]:
            new_class[cur]=new_class[prev]+1
        else:
            new_class[cur]=new_class[prev]

    return new_class


def build_suffix(string):
    order=char_sort(string)
    myclass=classes(string,order)
    l=1
    while l<len(string):
        order=sort_doubled(l,myclass,string,order)
        myclass=update_class(order,myclass,l)
        l=2*l
    return order
def find_pattern(string,pattern):

    for i in build_suffix(string):
        suffix = string[i:]
        if pattern == suffix[:len(pattern)]:
            print(i)

string = input()
n = input()
pattern=input()
pattern=pattern.split(" ")
for i in pattern:
    find_pattern(string,i)


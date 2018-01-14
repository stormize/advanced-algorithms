#python 3
def create_suffix(string):
    suffix=[None]*(len(string))
    for i in range(0,len(string)):
        suffix[i]=string[i:]
    suffix.sort()
    return suffix
suffix =create_suffix(input())
n=input()
pttern=input()

for i in suffix:
    print(i)
    if pttern ==i[:len(pttern)]:
        print(len(suffix)-len(i))


# python 3
string = input()
array = sorted([[string[i:],i] for i in range(len(string))])
for i in array:
    print(i[1])


# python 3
import itertools


def prefix(s):
    result = []
    border = 0
    result.append(0)
    for i in range(1, len(s)):
        while border > 0 and not s[i] == s[border]:
            border = result[border - 1]
        if s[border] == s[i]:
            border += 1
        else:
            border = 0
        result.append(border)
    return result


def kmp(prefix, s, p):
    result = []
    prefix = prefix(p);

    k=0
    for i  in range(0,len(s) ):
        while k > 0 and not s[i] == p[k]:
            k = prefix[k - 1]
        if s[i] == p[k]:
            k += 1
        if k == len(p):
            result.append(i - len(p) + 1)
            k = prefix[k - 1]

    return result
part=input()
all=input()
result = kmp(prefix, all, part)
for i in result:
 print(i);

# python3
import sys
s=input()
result=""
soso = sorted([s[i:]+s[:i] for i in range (len(s))])
for i in soso:
  result+= i[len(i)-1]
print(result)









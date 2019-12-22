from sys import stdin
n = int(stdin.readline())
s,t = map(str,input().split())
newstr = []
for i in range(n):
    newstr.append(s[i])
    newstr.append(t[i])
print("".join(newstr))
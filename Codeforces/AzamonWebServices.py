from sys import stdin
def solve(a,b):
    t,s = list(a),"".join(sorted(a))
    for i in range(len(a)):
        if t[i] != s[i]:
            y = a.rindex(s[i])
            t[i],t[y] = t[y],t[i]
            break
    z = "".join(t)
    return(z if z<b else "---")
for _ in range(int(stdin.readline())):
    s, c = map(str,stdin.readline().split())
    print(solve(s,c))
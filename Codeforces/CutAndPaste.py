def solve(s,x):
    n = len(s)
    mod = 10**9 + 7
    for i in range(x):
        n += (n-i-1)*(int(s[i])-1)
        n %= mod
        if len(s) < x:
            s += s[i+1:]*(int(s[i])-1)
    return n
for _ in range(int(input())):
    x = int(input())
    s = input()
    print(solve(s,x))
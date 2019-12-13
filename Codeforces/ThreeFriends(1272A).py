def calc(a,b,c):
    return abs(a-b) + abs(b-c) + abs(c-a)
n = int(input())
for z in range(n):
    a,b,c = map(int,input().split())
    ans = calc(a,b,c)
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                na = a + i
                nb = b + j
                nc = c + k
                ans = min(ans,calc(na,nb,nc))
    print(ans)
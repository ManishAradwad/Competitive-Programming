n = int(input())
numbs = [int(x) for x in input().split()]
pref = [1]*n
suf = [1]*n
ans = 1
for i in range(n-2,-1,-1):
    if (numbs[i+1]>numbs[i]):
        suf[i] = suf[i+1] + 1
    ans = max(suf[i],ans)
for i in range(1,n):
    if (numbs[i-1] < numbs[i]):
        pref[i] = pref[i-1] + 1
    ans = max(ans,pref[i])
for i in range(1,n-2):
    if numbs[i] < numbs[i+2]:
        ans = max(ans,pref[i]+suf[i+2])
print(ans)

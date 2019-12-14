n = int(input())
magnets = [input() for i in range(n)]
grps = 1
for i in range(1,n):
    if magnets[i-1] != magnets[i]:
        grps += 1
print(grps)

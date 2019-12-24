n = int(input())
bricks = [int(x) for x in input().split()]
if 1 not in bricks:
    ans = -1
else:
    counter = 1
    ans = 0
    for i in range(n):
        if bricks[i] == counter:
            counter += 1
        else:
            ans += 1
print(ans)
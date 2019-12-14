from sys import stdin
n, k = map(int,stdin.readline().split())
if k <= (n+1) / 2:
    print(2 * k - 1)
else:
    print((k - (n+1) // 2) * 2)
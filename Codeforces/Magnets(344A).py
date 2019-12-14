from sys import stdin
n = int(stdin.readline())
a = int(stdin.readline())
ans = 1
for i in range(n-1):
    b = int(stdin.readline())
    if a != b:
        ans += 1
    a = b
print(ans)
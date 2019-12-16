from sys import stdin
n = int(stdin.readline())
if n % 2 == 0:
    print(n//2)
else:
    print(((n-1)//2)-n)
result, n = map(int,input().split())
for i in range(n):
    if result % 10 > 0:
        result -= 1
    elif result % 10 == 0:
        result //= 10
print(result)
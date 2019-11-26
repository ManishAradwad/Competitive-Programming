n = int(input())
steps = 0
for i in range(5,0,-1):
    steps += n // i
    n %= i
print(steps)
import math
n = int(input())
fact = math.factorial(n)
ans = 0
while(fact % 10 == 0):
    ans += 1
    fact = fact//10
print(ans)
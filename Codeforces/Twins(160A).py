n = int(input())
coins = sorted([int(x) for x in input().split()])
sum1 = count = 0
while(sum1 <= sum(coins)):
    sum1 += coins.pop()
    count += 1
print(count)

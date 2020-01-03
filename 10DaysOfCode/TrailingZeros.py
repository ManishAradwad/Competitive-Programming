def trailingzeros(x):
    ans = 0
    power = 5
    while(x//power > 0):
        ans += x//power
        power *= 5
    return ans
n = int(input())
print(trailingzeros(n))
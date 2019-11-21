n = int(input())
coll = [4,7,47,74,444,447,474,477,744,747,777]
for i in coll:
    if n % i == 0:
        print("YES")
        exit()
print("NO")
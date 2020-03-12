n = int(input())
x = map(int,input().split())
y = map(int,input().split())
ans = 0
for i in range(1,n+1):
    if i in x or i in y: 
        ans += 1
if ans == n:
    print("I become the guy.")
else: print("Oh, my keyboard!")
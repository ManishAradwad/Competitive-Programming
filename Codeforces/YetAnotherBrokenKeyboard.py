n, k = map(int,input().split())
n_str = input()
k_str = set(x for x in input().split())
ans = 0
count = 0
for i in n_str:
    if i in k_str:
        count += 1
    else:
        ans += count*(count+1)//2
        count = 0
ans += count*(count+1)//2
print(ans)
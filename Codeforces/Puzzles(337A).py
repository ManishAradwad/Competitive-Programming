n, m = map(int,input().split())
puzzles = sorted([int(x) for x in input().split()])
min_puzz = 1000
for i in range(m-n+1):
    temp = puzzles[i:i+n]
    min_puzz = min(min_puzz,max(temp)-min(temp))
print(min_puzz)


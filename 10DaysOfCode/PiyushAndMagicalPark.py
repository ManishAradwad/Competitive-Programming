n,m,k,s = map(int,input().split())
park = []

for i in range(n):
    temp = [str(x) for x in input().split()]
    park.append(temp)

for i in range(n):
    for j in range(m):
        if s<k:
            print('No')
            exit()
        if park[i][j] == '.':
            s -= 2 if j == m-1 else 3
        elif park[i][j] == '*':
            s += 5 if j == m-1 else 4
        elif park[i][j] == '#':
            break

print("Yes\n"+str(s) if s >= k else "No")
matrix=[]
for i in range(5):
  temp=[int(x) for x in input().split()]
  matrix.append(temp)
for i in range(5):
  for j in range(5):
    if matrix[i][j]==1:
        print(abs(i-2)+abs(j-2))

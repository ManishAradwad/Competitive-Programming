n = int(input())
number = 0
caps = []
for i in range(n):
    i,j = map(int,input().split())
    number = number + j - i
    caps.append(number) 
print(max(caps))
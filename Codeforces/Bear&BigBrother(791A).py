a, b = map(int,input().split())
yrs = 0
while(a<=b):
    yrs+=1
    a*=3
    b*=2
print(yrs)
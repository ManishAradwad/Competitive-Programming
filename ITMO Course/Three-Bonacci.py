with open("input.txt",'r') as input:
    a0,a1,a2,n = map(int,input.readline().split())
with open("output.txt",'w') as output:
    Tn = 0
    while(n!=0):
        Tn = a2 + a1 - a0
        a0 = a1
        a1 = a2
        a2 = Tn
        n-=1
    output.write(str(a0))
    output.write('\n')
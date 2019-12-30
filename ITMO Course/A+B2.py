with open("input.txt",'r') as input:
    a, b = map(int,input.readline().split())
with open("output.txt",'w') as output:
    output.write(str(a+b**2))
    output.write('\n')
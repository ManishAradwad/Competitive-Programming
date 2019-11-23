n = int(input())
groups = sorted([int(x) for x in input().split()],reverse=True)
fours = groups.count(4)
threes = groups.count(3)
twos = groups.count(2)
ones = groups.count(1)
taxies = fours + threes
ones -= threes
taxies += twos // 2
if(twos%2>0):
    taxies+=1
    ones-=2
if(ones>0):
    taxies+=(ones//4)
    if(ones%4>0):
        taxies+=1
print(taxies)
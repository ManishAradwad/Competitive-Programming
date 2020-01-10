from itertools import permutations
n = int(input())
p = tuple(int(x) for x in input().split())
q = tuple(int(x) for x in input().split())
permuts = list(permutations(range(1,n+1)))
print(abs(permuts.index(p) - permuts.index(q)))            
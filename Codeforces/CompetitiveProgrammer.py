from itertools import permutations
import math
from sys import stdin
n = int(stdin.readline())
for i in range(n):
    inp = int(stdin.readline())
    if inp == 0:
        print("red")
    else:
        permList = permutations(str(inp))
        for perm in list(permList):
            if int("".join(perm)) % 60 == 0:
                print("red")
                break
            else:
                print("cyan")
                
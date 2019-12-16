from collections import Counter
from sys import stdin
for _ in range(int(stdin.readline())):
    d = Counter(stdin.readline())
    lr,ud = min(d['L'],d['R']) , min(d['U'],d['D'])
    lr = lr if ud else min(lr,1)
    ud = ud if lr else min(ud,1)
    print(f"{2 * (lr+ud)} \n{lr*'L' + ud*'U' + lr*'R' + ud*'D'}")
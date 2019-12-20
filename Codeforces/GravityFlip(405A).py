from sys import stdin
n = int(stdin.readline())
boxes = sorted([int(x) for x in stdin.readline().split()])
print(*boxes)

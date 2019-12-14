from sys import stdin
n, h = map(int,stdin.readline().split())
count = 0
for i in stdin.readline().split():
    i = int(i)
    if i > h:
        count += 2
    else:
        count += 1
print(count)
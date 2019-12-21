from sys import stdin
n = int(stdin.readline())
numbers = [x for x in stdin.readline().split()]
for number in numbers:
    sum = 0
    for i in number:
        if i != '\n':
            sum += int(i)   
    print(sum)
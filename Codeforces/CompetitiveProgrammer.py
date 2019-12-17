from sys import stdin
n = int(stdin.readline())
for i in range(n):
    number = stdin.readline()
    digits = []
    for digit in number:
        if digit != "\n":
            digits.append(int(digit))
    even = 0
    for i in digits:
        if i % 2 == 0:
            even += 1
    if sum(digits) % 3 == 0 and digits.count(0) >= 1 and even >= 2:
        print("red")
    else: print("cyan")

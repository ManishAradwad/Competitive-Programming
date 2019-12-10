n = int(input())
numbs = []
for i in range(1000,9001):
    i = str(i)
    if i.count('0') < 2 and i.count('1') < 2 and i.count('2') < 2 and i.count('3') < 2 and i.count('4') < 2 and i.count('5') < 2 and i.count('6') < 2 and i.count('7') < 2 and i.count('8') < 2 and i.count('9') < 2:
        numbs.append(int(i))
numbs.append(9012)
for i in numbs:
    if n < i:
        print(i)
        break
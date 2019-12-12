n = int(input())
str = input()
if str.count('D') > str.count('A'):
    print("Danik")
elif str.count('A') > str.count('D'):
    print("Anton")
else:
    print("Friendship")
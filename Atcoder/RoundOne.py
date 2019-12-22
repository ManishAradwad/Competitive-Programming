number1 = int(input())
number2 = int(input())
choices = [1,2,3]
choices.remove(number1)
choices.remove(number2)
print(*choices)
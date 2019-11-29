n = int(input())
s1 = "I hate"
s2 = "I love"
result = []
for i in range(n):
    if(i&1):
        result.append(s2)
    else:
        result.append(s1)
    if (i != n-1):
        result.append("that")
result.append("it")
print(" ".join(result))
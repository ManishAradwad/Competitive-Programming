a,b = input(),input()
final = []
for i in range(len(a)):
    m = int(a[i])
    n = int(b[i])
    result = int((m and not n) or (not m and n))
    final.append(str(result))
print("".join(final))

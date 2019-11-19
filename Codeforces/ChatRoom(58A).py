s = input()
i = -1
for c in "hello":
  i = s.find(c,i+1)
  if i == -1:
    print("NO")
    exit()
print("YES")
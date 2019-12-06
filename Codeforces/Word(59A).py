word = input()
up = 0
lo = 0
for i in word:
    if i.isupper(): up+=1
    else: lo+=1
if lo>=up: print(word.lower())
else: print(word.upper())
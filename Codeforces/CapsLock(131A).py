str = input()
res = []
if str.isupper() or (str[0].islower() and str[1:].isupper()):
    for i in str:
        if i.isupper(): res.append(i.lower())
        else: res.append(i.upper())
    print("".join(res))
elif len(str) == 1:
    print(str.upper())
else: 
    print(str)
exp = input()
res = []
for i in range(len(exp)):
    res.append(exp[i])
    if exp[i] == '-':
        i += 1
        res.append(exp[i])
        i += 1
        while(i < len(exp) and exp[i] == '0'):
            res.append("+0")
            i+=1
        if i < len(exp) and exp[i] >= '1' and exp[i] <= '9':
            res.append['+']
        i -= 1
print(*res,sep="")
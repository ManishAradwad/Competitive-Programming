n = int(input())
for i in range(n):
    for j in range(n):
        if i < n//2:
            if j < n//2:
                if j == 0:
                    print('*',end='')
                else:
                    print(' ',end='')
            elif j == n//2:
                print('*',end='')
            else:
                if i == 0:
                    print('*',end = '')
        elif i == n//2:
            print("*",end='')
        else:
            if j == n-1 or j == n//2:
                print('*',end='')
            elif i == n-1 :
                if j<=n//2 or j == n-1:
                    print('*',end='')
                else:
                    print(' ',end='')
            else:
                print(' ',end='')
    print()
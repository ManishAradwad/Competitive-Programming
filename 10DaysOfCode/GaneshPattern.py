n = int(input())
print('*'+ ' ' * int((n-3)/2) + '*' * int((n+1)/2))
for _ in range((n-3)//2 + 1):
    print('*'+' '*int((n-3)/2)+'*'+' '*int((n-3)/2))
print('*' * n)
for _ in range((n-3)//2 + 1):
    print(' '*int((n-1)/2)+'*'+' '*int((n-3)/2)+'*')
print('*'*int((n+1)/2) + ' '*int((n-3)/2) + '*')
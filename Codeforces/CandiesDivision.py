for _ in range(int(input())):
    n, k = map(int,input().split())
    full = n - n % k    
    full += min(n%k,k//2)
    print(full)
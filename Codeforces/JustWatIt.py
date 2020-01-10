for _ in range(int(input())):
    n = int(input())
    cakes = [int(x) for x in input().split()] 
    yasser = sum(cakes)
    check = True
    for i in range(n):
        for j in range(n):
            if i < j:
                adel = cakes[i:j]
                if sum(adel) >= yasser:
                    check = False
                    break
    print("YES" if check else "NO")
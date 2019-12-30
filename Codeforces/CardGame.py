for _ in range(int(input())):
    n, k1, k2 = map(int,input().split())
    first = [int(x) for x in input().split()]
    second = [int(x) for x in input().split()]
    print("YES" if n in first else "NO")    
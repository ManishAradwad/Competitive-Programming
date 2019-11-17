n = int(input())
stones = input()
print(sum([1 for i in range(n-1) if stones[i]==stones[i+1]]))
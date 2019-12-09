n = int(input())
nums = [int(x) for x in input().split()]
count = 1
temp = 1
for i in range(n):
    if i > 0:
        if nums[i] >= nums[i+1]:
            count += 1
            temp = max(temp,count)
        else:
            count = 1
print(temp)
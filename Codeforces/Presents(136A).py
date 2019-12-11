# n = int(input())
# numbs = [int(x) for x in input().split()]
# dic = {}
# new_dic = {}
# res = []
# for i in range(1,n+1):
#     dic[i] = numbs[i-1]
# for key,value in dic.items():
#     new_dic[value] = key
# for i in sorted(new_dic.keys()):
#     res.append(new_dic[i])
# print(*res)

n = int(input())
numbs = [*map(int,input().split())]
for i in range(1,n+1):
    print(numbs.index(i)+1)
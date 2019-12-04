# num = 0 
# for i in input():
#     if i == '4' or i == '7':
#         num+=1
# print("YES" if num==4 or num==7 else "NO")
num = input()
m = num.count("4") + num.count("7")
print("YES" if m == 4 or m == 7 else "NO")
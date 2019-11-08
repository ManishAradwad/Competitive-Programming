"""
#My solution:

n = int(input())
all_problems = []
for i in range(n):
    indiv_problem = [int(j) for j in input()]
    all_problems.append(indiv_problem)

prob_solved = 0

for i in all_problems:
    count = 0
    for j in range(n):
        if i[j] == 1:
            count = count+1
    if count>=2:
        prob_solved = prob_solved + 1

print(prob_solved)

"""

n = int(input())
count = 0

while(n>0):
    n-=1
    k = input()
    if k.count('1') > 0:
        count+=1
print(count)

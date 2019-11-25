result = []
for i in range(int(input())):
    action = input().split()
    for i in range(1,len(action)):
        action[i] = int(action[i])
    if action[0] == "insert":
        result.insert(action[1],action[2])
    if action[0] == "print":
        print(result)
    if action[0] == "append":
        result.append(action[1])
    if action[0] == "remove":
        result.remove(action[1])
    if action[0] == "sort":
        result = sorted(result)
    if action[0] == "pop":
        result.pop()
    if action[0] == "reverse":
        result.reverse()
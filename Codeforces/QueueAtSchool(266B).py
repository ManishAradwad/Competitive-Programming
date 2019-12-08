n,m = map(int,input().split())
string = input()
for i in range(m):
    if "BG" in string:
        string = string.replace("BG","GB")
print(string)
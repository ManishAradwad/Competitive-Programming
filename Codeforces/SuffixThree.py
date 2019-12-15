from sys import stdin
for i in range(int(stdin.readline())):
    sent = stdin.readline()
    if sent.endswith("po\n") : print("FILIPINO")
    elif sent.endswith("desu\n") or sent.endswith("masu\n"): print("JAPANESE")
    elif sent.endswith("mnida\n"): print("KOREAN")
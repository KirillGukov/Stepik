n = int(input())
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(j + 1, end='')
    for k in range(i - 1, 0, -1):
        print(k, end="")
        num += 1
    print()
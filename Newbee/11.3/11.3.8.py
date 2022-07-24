n = int(input())
s = []
k = [input() for _ in range(n)]
b = int(input())
for i in k:
    if len(i) < b:
        continue
    if len(i) >= b:
        print(i[b - 1], end="")
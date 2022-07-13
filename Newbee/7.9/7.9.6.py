n = int(input())
sm = 0
pr = 1
for i in range(1, n + 1):
    pr *= i
    sm += pr
print(sm)
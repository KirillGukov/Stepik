m, n = int(input()), int(input())
for i in range(m, n + 1):
    if i % 17 == 0:
        print(i)
    if i % 10 == 9 or i == 9:
        print(i)
    if i % 15 == 0:
        print(i)
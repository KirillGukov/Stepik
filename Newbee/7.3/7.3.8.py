num = 1
n = int(input())
for i in range(2, n + 1):
    if i % 2 == 0:
        num -= i
    elif i % 2 == 1:
        num += i
print(num)

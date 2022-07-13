n = int(input())
num1 = 1
num2 = 0
for i in range(1, n + 1):
    num = int(input())
    if num > num1:
        num2 = num1
        num1 = num
    elif num > num2:
        num2 = num
print(num1)
print(num2)

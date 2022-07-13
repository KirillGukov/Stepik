num1 = 0
num2 = 1
n = int(input())
for i in range(n):
    num1, num2 = num2, num1 + num2
    print(num1, end=" ")
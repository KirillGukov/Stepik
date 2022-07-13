from math import *
num = 0
n = int(input())
for i in range(1, n):
    num = num + (1 / (i + 1))
num2 = num + 1 - log(n)
print(num2)

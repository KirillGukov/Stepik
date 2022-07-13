num = 0
a = int(input())
while a >= 25:
    a -= 25
    num += 1
while a >= 10:
    a -= 10
    num += 1
while a >= 5:
    a -= 5
    num += 1
while a >= 1:
    a -= 1
    num += 1
print(num)
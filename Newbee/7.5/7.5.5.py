num = chi = int(input())
a = 0
while num != 0:
    last_num = num % 10
    a += 1
    num = num // 10
print(chi % (10 ** (a - 1)) // (10 ** (a - 2)))
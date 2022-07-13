num = int(input())
while num >= 10:
    s = num % 10
    num = num // 10
    num += s
print(num)
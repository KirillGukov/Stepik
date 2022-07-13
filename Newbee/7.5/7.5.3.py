mn = 9
mx = 0
num = int(input())
while num != 0:
    last_num = num % 10
    if last_num > mx:
        mx = last_num
    if last_num < mn:
        mn = last_num
    num = num // 10
print("Максимальная цифра равна", mx)
print("Минимальная цифра равна", mn)
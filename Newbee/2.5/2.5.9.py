n = int(input())
a = (n % (10 ** 4)) // 10 ** (4 - 1)
b = (n % 10 ** (4 - 1)) // 10 ** (4 - 2)
c = (n % 10 ** (4 - 2)) // 10 ** (4 - 3)
d = (n % 10 ** (4 - 3)) // 10 ** (4 - 4)
print("Цифра в позиции тысяч равна", a)
print("Цифра в позиции сотен равна", b)
print("Цифра в позиции десятков равна", c)
print("Цифра в позиции единиц равна", d)
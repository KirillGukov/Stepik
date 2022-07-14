a = input()
s = 0
for i in range(0, 10):
    if str(i) in a:
        s += 1
if s > 0:
    print("Цифра")
else:
    print("Цифр нет")
a = int(input())
if 1 <= a <= 3:
    print(a * "I")
elif a == 4:
    print("IV")
elif a == 5:
    print("V")
elif 6 <= a <= 8:
    print("V", (a - 5) * "I", sep="")
elif a == 9:
    print("IX")
elif a == 10:
    print("X")
else:
    print("ошибка")
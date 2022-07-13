from math import *
a, b, c = float(input()), float(input()), float(input())
d = (b ** 2) - 4 * a * c
if d > 0:
    min((((- b + (d ** 0.5)) / (2 * a))), (((- b - (d ** 0.5)) / (2 * a))))
    max((((- b + (d ** 0.5)) / (2 * a))), (((- b - (d ** 0.5)) / (2 * a))))
elif d == 0:
    print((- b) / (2 * a))
else:
    print("Нет корней")

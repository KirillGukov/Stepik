a, b, c = int(input()), int(input()), int(input())
if a < b < c:
    print(b)
elif b < a < c:
    print(a)
elif c < b < a:
    print(b)
elif c < a < b:
    print(a)
else:
    print(c)
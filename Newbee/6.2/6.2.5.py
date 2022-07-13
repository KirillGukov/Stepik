a, b, c = input(), input(), input()
n = min(len(a), len(b), len(c))
x = max(len(a), len(b), len(c))
d = len(a) + len(b) + len(c) - n - x
if x - d == d - n:
    print("YES")
else:
    print("NO")
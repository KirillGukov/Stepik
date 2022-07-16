a = int(input())
s = ""
while a >= 1:
    s = str(a % 2) + s
    a //= 2
print(s)
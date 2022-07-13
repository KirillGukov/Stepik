c = 0
for i in range(1, 11):
    num = int(input())
    if num % 2 == 0:
        c += c
    if num % 2 == 1:
        c += 1
if c >= 1:
    print("NO")
else:
    print("YES")

s = 0
for i in range(1, 8):
    i = int(input())
    if i % 2 == 0:
        s = s + i
if s > 0:
    print(s)
else:
    print("0")

a = input()
s = 0
for i in range(len(a) - 1):
    if a[i] == a[i + 1]:
        s += 1
print(s)

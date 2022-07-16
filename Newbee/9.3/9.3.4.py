a = input()
k = 0
s = a.lower()
for i in a:
    if i.upper() != i.lower() and i in s:
        k += 1
print(k)
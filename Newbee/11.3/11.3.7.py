n = int(input())
s = []
for i in range(n):
    k = int(input())
    s.append(k)
del s[1::2]
print(s)
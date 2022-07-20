n = int(input())
s = []
l = 0
for i in range(n):
    k = int(input())
    l += k
    s.append(l)
    l = k
print(s[1::])
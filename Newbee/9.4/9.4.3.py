n = int(input())
s = 0
for i in range(n):
    a = input()
    if a.count("11") >= 3:
        s += 1
print(s)
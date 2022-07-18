tex = input()
s = 0
l = len(tex)
for i in range(l):
    if "0" <= tex[i] <= "9":
        s += 1
print(s)
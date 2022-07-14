a = input()
s = 0
p = 0
for i in a:
    if str(i) == "+":
        s += 1
    if str(i) == "*":
        p += 1
print("Символ + встречается", s, "раз" )
print("Символ * встречается", p, "раз" )
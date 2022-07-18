text = input()
a, b = 0, 0
for i in text:
    if text.count(i) >= a:
        a = text.count(i)
        b = i
print(b)
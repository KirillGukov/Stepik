a = int(input())
text = input()
for i in text:
    s = ord(i) - a
    if s < 97:
        s += 26
        s = chr(s)
    else:
        s = chr(s)
    print(s, end="")

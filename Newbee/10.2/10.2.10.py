n = input()
if n.count("f") == 1:
    print("-1")
if n.count("f") == 0:
    print("-2")
if n.count("f") >= 2:
    l = n.replace('f', ' ', 1)
    print(l.find('f'))
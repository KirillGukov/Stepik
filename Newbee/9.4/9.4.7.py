text = input()
if text.count("f") == 1:
    print(text.find("f"))
if text.count("f") > 1:
    print(text.find("f"), text.rfind("f"))
if text.count("f") == 0:
    print("NO")
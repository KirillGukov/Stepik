l = input()
first = l.find("h")
last = l.rfind("h")
print(l[0:l.find("h") + 1], l[l.rfind("h") - 1: l.find("h"): -1], l[last:], sep="")

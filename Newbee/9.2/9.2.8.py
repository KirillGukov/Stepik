a = input()
s = len(a)
print(a[(s - (s // 2)):], a[0: (s - (s // 2))], sep="")

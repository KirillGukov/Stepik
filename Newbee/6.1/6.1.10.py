a = int(input())
b = (a % (10 ** 3)) // 10 ** 2
c = (a % (10 ** 2)) // 10
d = (a % 10) // 1
n = min(b, c, d)
k = max(b, c, d)
if k - n == (b + c + d - n - k):
    print("Число интересное")
else:
    print("Число неинтересное")
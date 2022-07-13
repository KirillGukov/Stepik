a = int(input())
b = int(input())
c = int(input())
if b < a + c and a < b + c and c < a + b:
    print("YES")
else:
    print("NO")
num = int(input())
last = num % 10
sen = True
while num != 0:
    last_num = num % 10
    if last_num < last:
        sen = False
    last = last_num
    num = num // 10
if sen == True:
    print("YES")
else:
    print("NO")
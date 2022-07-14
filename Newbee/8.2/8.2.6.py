n = int(input())
three, last_num, chi, sum5, zero5, pr7, last = 0, 0, 0, 0, 0, 1, n % 10
while n >= 1:
    x = n % 10
    if x == 3:
        three += 1
    if x == last:
        last_num += 1
    if x % 2 == 0:
        chi += 1
    if x > 5:
        sum5 += x
    if x > 7:
        pr7 *= x
    if x == 0:
        zero5 += 1
    if x == 5:
        zero5 += 1
    n //= 10
print(three)
print(last_num)
print(chi)
print(sum5)
print(pr7)
print(zero5)
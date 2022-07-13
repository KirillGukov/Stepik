sm = col = 0
pr = 1
num = chi = int(input())
while num != 0:
    last_num = num % 10
    sm += last_num
    col += 1
    pr *= last_num
    num = num // 10
first = chi // (10 ** (col - 1))
last = chi % 10
av = sm / col
fir_las = first + last
print(sm, col, pr, av, first, fir_las, sep="\n")
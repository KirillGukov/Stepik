a, b = int(input()), int(input())
max_sum_del = 0
sum_del = 0
for i in range(a, b + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += j
        if count >= max_sum_del:
            max_sum_del = count
            sum_del = i
print(sum_del, max_sum_del)
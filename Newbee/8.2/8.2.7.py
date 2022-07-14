for i in range(1, 33):
    for j in range(1, 33):
        for k in range(1, 33):
            for l in range(1, 33):
                if i != j and i != j and i != k and i != l and j != k and j != l and k != l and (i ** 3) + (j ** 3) == (k ** 3) + (l ** 3):
                    print((i ** 3) + (j ** 3))


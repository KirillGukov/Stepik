a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print("Равносторонний")
elif a != b != c and a != c != b and b != c != a:
    print("Разносторонний")
else:
    print("Равнобедренный")
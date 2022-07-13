a = input()
b = input()
if a == "красный" and b == "красный":
    print("красный")
elif a == "синий" and b == "синий":
    print("синий")
elif a == "желтый" and b == "желтый":
    print("желтый")
elif (a == "красный" and b == "синий") or (a == "синий" and b == "красный"):
    print("фиолетовый")
elif (a == "синий" and b == "желтый") or (a == "желтый" and b == "синий"):
    print("зеленый")
elif(a == "желтый" and b == "красный") or (a == "красный" and b == "желтый"):
    print("оранжевый")
else:
    print("ошибка цвета")
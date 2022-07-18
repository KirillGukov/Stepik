text = input()
a = text.find("h")
b = text.rfind("h")
print(text[0:a], text[b + 1:len(text)], sep="")
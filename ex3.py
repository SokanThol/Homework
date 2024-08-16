# Enter text and check if it contains capital letter or not
text = input("Enter text :")
result = ""
for i in range(len(text)):
    if text[i] == text[i].upper():
        result += text[i]
print(result)
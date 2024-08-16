# We have text = "3 4 5 6"
# Q1 - display number 1 by one without space
# Q2 - Sum all number (Total: 18)
text = "3 4 5 6"
sum = ""
for i in range(len(text)):
    if text[i] != " ":
        sum += text[i]
print(sum)
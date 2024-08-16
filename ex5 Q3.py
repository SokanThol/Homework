# Ex5 - String 
# We have text = "454639"
# Q3 - Sum only even number 
text = "454639"
sum = 0
for i in range(len(text)):
    if i % 2 == 0:
        sum += int(text[i])
print(sum)

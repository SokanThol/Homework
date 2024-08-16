# Ex10 - Number
# Enter 5 numbers and find maximum and minimum value
# Example:
# 1
# 5
# 6
# 7
# 0
# output : Max = 7, Min = 0
combo = ''
for i in range(5):
    number = int(input("Enter number :"))
    combo += str(number)
max = 0
min = number
for j in range(len(combo)):
    if int(combo[j]) > max:
        max = int(combo[j])
    if int(combo[j]) < min:
        min = int(combo[j])
print(max,min)
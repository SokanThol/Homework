# Ex5 - String 
# We have text = "454639"
# Q1 - Count odd and even number in text
# Q2 - Sum all number 
# Q3 - Sum only even number 
# Q4 - Reverse
text = "454639"
odd_count = 0
even_count = 0
for i in range(len(text)):
    if i % 2 == 0:
       even_count += 1
    elif i % 2 == 1:
        odd_count += 1
print("odd_count", odd_count)
print("even_count", even_count)



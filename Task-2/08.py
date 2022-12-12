str_in = input("Enter a string: ")

count_letter = 0
count_digit = 0

for i in str_in:
    if i.isdigit():
        count_digit += 1
    elif i.isalpha():
        count_letter += 1

print("Letters", count_letter)
print("Digits", count_digit)
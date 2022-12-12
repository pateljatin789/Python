counter = 1
while counter <=5:
    number = int(input("Guess the lucky number: "))
    counter += 1
    if number == 3:
        print("Good Guess")
    else:
        print("Try again")
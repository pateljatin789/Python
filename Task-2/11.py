counter = 1
while counter <=5:
    number = int(input("Guess the lucky number: "))
    counter += 1
    if number == 3:
        print("Good Guess")
        break
    else:
        print("Try again")     
else:
    print("Sorry but that was not very successful")
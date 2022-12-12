while True:
    answer = input("Do you want to guess number: ").upper()
    if answer == "YES":
        number = int(input("Guess the lucky number: "))
        if number == 3:
            print("You are a Winner")
            break
        else:
            print("Try again")
            continue
    elif answer == "NO":
        print("Thank you")
        break
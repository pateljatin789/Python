print("Enter 1 - Addition\nEnter 2 - Subtraction\nEnter 3 - Division\nEnter 4 - Multiplication\nEnter 5 - Average")
Task_input = int(input("Enter the Task: "))

num1 = int(input("Enter value 1: "))
num2 = int(input("Enter value 2: "))

if Task_input == 1:
    num3 = num1 + num2
elif Task_input == 2:
    num3 = num1 - num2
elif Task_input == 3:
    num3 = num1 / num2
elif Task_input == 4:
    num3 = num1 * num2
elif Task_input == 5:
    num1a = int(input("Enter value 3: "))
    num2a = int(input("Enter value 4: "))
    num3 = (num1+num2+num1a+num2a)/4
else:
    print("Invalid input")

if num3 >= 0:
    print(f"output is {num3}")
else:
    print(f"Output {num3} is nagative value")
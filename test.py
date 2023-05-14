# import modules
import modules.addition as addition, modules.subtraction as subtraction, modules.multiplication as multiplication, modules.division as division

# 9. continue program until user exits the app
while True:
    # 6. print app functions to user
    print('''A. Addition
B. Subtraction
C. Multiply
D. Divide
E. Exit''')

    # 7. get choice from users
    choice = input("Enter choice: ").upper()

    # 8. use conditionals to make decision based on user input
    if choice == "A":
        print("Addition")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        addition.add(a,b)
    elif choice == "B":
        print("Subtraction")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        subtraction.sub(a,b)
    elif choice == "C":
        print("Multiplication")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        multiplication.multiply(a,b)
    elif choice == "D":
        print("Divsion")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        division.divide(a,b)
    elif choice == "E":
        print("Program Ended")
        quit()
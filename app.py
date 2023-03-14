# define functions needed for app - add, sub, multiplication & division

# addition function
def add(a, b):
    answer = a + b 
    # print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")
    print(f"{a} + {b} = {answer} \n")

# subtraction function
def sub(a,b):
    answer = a - b
    # print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")
    print(f"{a} - {b} = {answer} \n")

# multiplication function
def multiply(a,b):
    answer = a * b
    # print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")
    print(f"{a} * {b} = {answer} \n")

# division function
def divide(a,b):
    answer = a / b
    # print(str(a) + " / " - str(b) + " = " + str(answer) + "\n")
    print(f"{a} / {b} = {answer}")


# continue program until user exits the app
while True:
    # print app functions to user
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiply")
    print("D. Divide")
    print("E. Exit") 

    # get data from users
    choice = input("Input your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        add(a,b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        sub(a,b)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        multiply(a,b)
    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        divide(a,b)
    elif choice == "e" or choice == "E":
        print("Program ended")
        quit()





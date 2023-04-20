
# functions
def print_menu():
    print("=============")
    print("[1] Sum")
    print("[2] Subtract")
    print("[3] Multiplication")
    print("[4] Division")
    print("=============")


# plain instructions
print_menu()
opt = input("select an option: ")
num1 = float(input("please provide the first number: "))
num2 = float(input("please provide the second number: "))

if opt == "1":
    total = float(num1 + num2)
    print("The total is " + total)
elif opt == "2":
    total = float(num1 - num2)
    print("The total is " + total)
elif opt == "3":
    total = float(num1 * num2)
    print("The total is " + total)
elif opt == "4":
    total = float(num1 / num2)
    print("The total is " + total)
else:
    print("Invalid operation")

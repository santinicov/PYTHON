#This is my basic calculator

print("Welcome to my lovely calculator!")

choice = input("Please choose an operator (+, -, *, /): ")

num1 = float(input("Type the first number: "))
num2 = float(input("Type the second number: "))

if choice == "+":
    plus = num1 + num2
    print(plus)
elif choice == "-":
    minus = num1 - num2
    print(minus)
elif choice == "*":
    mult = num1 * num2
    print(mult)
else:
    print("Wrong operator")
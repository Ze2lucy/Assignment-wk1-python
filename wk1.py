operator = input("Enter an operator(+ - * /):")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
    print(f"{operator}is not a valid operator")

print(f"{num1} {operator} {num2} = {result}")

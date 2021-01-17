# take two integers from user
num1 = int(input("enter first integer"))
num2 = int(input("enter second integer"))

print("press 1 for addition")
print("press 2 for subtraction")
print("press 3 for multipication")
print("press 4 for division")
operator = input(">")

if operator == "1":
     print(num1+num2)

if operator == "2":
    print(num1-num2)

if operator == "3":
    print(num1*num2)

if operator == "4":
    print(num1/num2)

import math

def add(num1,num2):
    sum = num1 + num2
    print(f"{num1} + {num2} = {sum}.")

def sub(num1,num2):
    sum = num1 - num2
    print(f"{num1} - {num2} = {sum}.")

def mult(num1,num2):
    product = num1 * num2
    print(f"{num1} * {num2} = {product}.")

def div(num1,num2):
    try:
        product = num1 / num2
        print(f"{num1} / {num2} = {product}.")
    except ZeroDivisionError:
        print("You cannot divide by 0")
    

while True:
    action = input("[A]dd, [S]ubtract, [M]ultiply, [D]ivide, or [Q]uit?")
    if action == 'A':
        try:
            num1 = float(input("First number?"))
        except ValueError:
            print("Please enter a valid number")
            continue
        try:
            num2 = float(input("Second number?"))
        except ValueError:
            print("Please enter a valid number")
            continue
        add(num1,num2)
    elif action == 'S':
        try:
            num1 = float(input("First number?"))
        except ValueError:
            print("Please enter a valid number")
            continue
        try:
            num2 = float(input("Second number?"))
        except ValueError:
            print("Please enter a valid number")
            continue
        sub(num1,num2)
    elif action == 'M':
        try:
            num1 = float(input("First number?"))
        except ValueError:
            print("Please enter a valid number")
            continue
        try:
            num2 = float(input("Second number?"))
        except ValueError:
            print("Please enter a valid number")
            continue
        mult(num1,num2)
    elif action == 'D':
        try:
            num1 = float(input("First number?"))
        except ValueError:
            print("Please enter a valid number")
            continue
        try:
            num2 = float(input("Second number?"))
        except ValueError:
            print("Please enter a valid number")
            continue
        div(num1,num2)
    elif action == 'Q':
        break
    else:
        print("That is not a valid option")
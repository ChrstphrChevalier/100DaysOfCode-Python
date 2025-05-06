import art

print(art.logo)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Divide by 0 impossible")
    else:
        return a / b

op = {
    '+': add,
    '-': sub,
    '*': mult,
    '/': divide
}

def first_number():
    while True:
        first_n = input("What's the first number?: ")
        try:
            first_n = float(first_n)
            return first_n
        except ValueError:
            print("Invalid number.")

def which_op():
    while True:
        print(" ".join(op.keys()))
        operate = input("Pick an operation: ")
        if operate in op:
            return operate
        print("Invalid Operator.")

def next_number():
    while True:
        next_n = input("What's the next number?: ")
        try:
            next_n = float(next_n)
            return next_n
        except ValueError:
            print("Invalid number.")


def calculator():
    first_n = first_number()
    operate = which_op()
    next_n = next_number()
    result = op[operate](first_n, next_n)
    print(f"{first_n} {operate} {next_n} = {result}")
    
    while True:
        choice = input(f"Type 'y' to continue calculating with {result}, type 'q' for quit or type 'n' to start a new calculation: ").lower()
        if choice == 'y':
            first_n = result
            operate = which_op()
            next_n = next_number()
            result = op[operate](first_n, next_n)
            print(f"{first_n} {operate} {next_n} = {result}")
        elif choice == 'n':
            first_n = first_number()
            operate = which_op()
            next_n = next_number()
            result = op[operate](first_n, next_n)
            print(f"{first_n} {operate} {next_n} = {result}")
        elif choice == 'q':
            print("Thanks, Goodbye.")
            break
        else:
            print("Invalid entry")
            
calculator()
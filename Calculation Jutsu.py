from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
Operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

f_num = int(input("Enter your first num: \n"))

Var = f_num

should_continue = True
while should_continue:
    operator = input("Choice operator: \n")
    next_num = int(input("Enter your next num: \n"))

    Var = Operations[operator](Var, next_num)
    print(Var)

    Should = input("Wanna continue the calculation(Y) or (N): \n")

    if Should == "N":
        should_continue = False
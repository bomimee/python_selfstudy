def add(n1, n2):
    return n1 + n2
def minus(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations ={
    "+": add,
    "-": minus,
    "*": multiply,
    "/": divide,
}


def calculator():
    continue_cal = True
    num1 = int(input("what is the first number? "))

    while continue_cal:
        op = input("pick an operation.\n + \n - \n * \n / \n")
        num2 = int(input("what is the second number? "))
        result = 0
        for key in operations:
            if op == key:
                result = operations[key](num1, num2)
        
        print(f"{num1} {op} {num2} = {result}")
        answer = input("you want to continue? ")
        if answer == 'y':
            num1 = result
        else:
            continue_cal = False
            calculator()
        
calculator()

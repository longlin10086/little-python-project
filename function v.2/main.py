#Add
def add(n1, n2):
    return n1 + n2


#Subtract
def subtract(n1, n2):
    return n1 - n2


#Multiply
def multiply(n1, n2):
    return n1 * n2


#Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate():
    num1 = int(input("What's the first number?: "))

    for operation in operations:
        print(operation)
    symbol = input("Pick the operation from the line above: ")

    num2 = int(input("What's the second number?: "))
    answer = operations[symbol](num1, num2)

    while True:
        print(f"{num1} {symbol} {num2} = {answer}")
        num1 = answer
        ans = input(f"Do you want to continue calculate with {answer}? Type 'yes' or 'no'.\n")
        if ans[0] == "n":
            break
        symbol = input("What operation do you want to continue?: ")
        num2 = int(input("What's the number?: "))
        answer = operations[symbol](answer, num2)
    calculate()


if __name__ == '__main__':
    calculate()





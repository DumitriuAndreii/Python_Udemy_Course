from art import logo
print(logo)

def addition(var1, var2):
    return var1 + var2

def subtraction(var1, var2):
    return var1 - var2

def multiplication(var1, var2):
    return var1 * var2

def division(var1,var2):
    return var1/var2




operations = {
    "+" : addition,
    "-" : subtraction,
    "*" : multiplication,
    "/" : division
}

def calculator():
    var1 = int(input("please choose your first number"))

    calc_over = 0
    while not calc_over:
        operation_symbol = input("choose an operation \n + \n - \n / \n * \n")
        var2 = int(input("please choose your second number"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(var1,var2)
        print(f"{var1} {operation_symbol} {var2} = {answer}")
        if input(f"type y to continue with {answer} or type 'n' to start a new calculus ") == 'y':
            var1 = answer
        else:
            calc_over =1
            calculator()

calculator()
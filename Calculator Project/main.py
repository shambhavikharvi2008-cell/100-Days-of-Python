

from art import logo

def add(n1, n2):

    return n1+n2
def substraction(n1,n2):
    return n1-n2
def multiplication(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

arithmetic_operation={
     "+":add,
     "-":substraction,
     "*":multiplication,
     "/":divide,
    }

def calculator():
    print(logo)
    should_accumulate=True
    try:
        first_number=float(input("What's the first number? "))
    except ValueError:
        print(None)
        return





    while should_accumulate:
        for symbol in arithmetic_operation:
            print(symbol)
        operation_symbol=input("pick your operation: ")
        second_number=float(input("What's the second number? "))


        answer=arithmetic_operation[operation_symbol](first_number,second_number)

        print(f"{first_number} {operation_symbol} {second_number} = {answer}")
        choice=input(f"Type 'y' to continue  calculating with {answer} or Type 'n' to start new calculation: ").lower()
        if choice=="y":
            first_number=answer
        else:
            should_accumulate=False
            print("\n"*20)
            calculator()

calculator()




















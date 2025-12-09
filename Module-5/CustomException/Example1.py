class InsufficientBalError(Exception):
    pass
bal=1000
amt=6000
try:
    print(7/0)
    if amt>bal:
        raise InsufficientBalError()
    else:
        bal=bal-amt
        print("Transaction Successful")
except InsufficientBalError:
    print("Insufficient Balance")
except ZeroDivisionError:
    print("Division by zero error occurred")
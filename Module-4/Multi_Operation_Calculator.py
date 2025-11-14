print("-------- Multi-Operation Calculator --------")

history = []


def add(a, b):
    result = a + b
    history.append(f"Add: {a} + {b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    history.append(f"Subtract: {a} - {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    history.append(f"Multiply: {a} * {b} = {result}")
    return result

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    result = a / b
    history.append(f"Divide: {a} / {b} = {result}")
    return result


def factorial(n):
    if n < 0:
        return "Factorial not possible!"
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    history.append(f"Factorial of {n} = {fact}")
    return fact


def is_prime(num):
    if num <= 1:
        history.append(f"Prime Check: {num} is NOT prime")
        return False
    
    for i in range(2, num):
        if num % i == 0:
            history.append(f"Prime Check: {num} is NOT prime")
            return False

    history.append(f"Prime Check: {num} is prime")
    return True



def power(base, exp=2):  # exp has a default value
    result = base ** exp
    history.append(f"Power: {base}^{exp} = {result}")
    return result



def total_sum(*nums):
    s = sum(nums)
    history.append(f"Sum of {nums} = {s}")
    return s



def show_details(**info):
    history.append(f"User Info: {info}")
    return info


while True:
    print("\n---- MENU ----")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Factorial")
    print("6. Prime Check")
    print("7. Power (default exp=2)")
    print("8. Sum of multiple numbers (*args)")
    print("9. User Details (**kwargs)")
    print("10. View History")
    print("11. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        print("Result:", add(a, b))

    elif ch == "2":
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        print("Result:", subtract(a, b))

    elif ch == "3":
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        print("Result:", multiply(a, b))

    elif ch == "4":
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        print("Result:", divide(a, b))

    elif ch == "5":
        n = int(input("Enter number: "))
        print("Result:", factorial(n))

    elif ch == "6":
        n = int(input("Enter number: "))
        if is_prime(n):
            print(n, "is a Prime Number")
        else:
            print(n, "is NOT a Prime Number")

    elif ch == "7":
        base = float(input("Enter base: "))
        exp = input("Enter exponent (press Enter for default): ")
        
        if exp == "":
            print("Result:", power(base))  
        else:
            print("Result:", power(base, int(exp)))

    elif ch == "8":
        nums = input("Enter numbers separated by space: ").split()
        nums = [float(i) for i in nums]
        print("Result:", total_sum(*nums))

    elif ch == "9":
        print("Enter details (name=..., age=..., city=...)")
        details = input("Enter key=value pairs separated by space: ").split()
        data = {}

        for d in details:
            k, v = d.split("=")
            data[k] = v
        
        print("User Details:", show_details(**data))

    elif ch == "10":
        print("\n----- HISTORY -----")
        for h in history:
            print(h)

    elif ch == "11":
        print("Exiting... Thank you!")
        break

    else:
        print("Invalid choice! Try again.")

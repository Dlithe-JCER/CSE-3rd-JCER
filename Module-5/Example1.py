# Develop simple function to read an integer from user and display its value
def read_integer():
    try:
        n=int(input("Enter an integer: "))
        print(n)  
    except:
        print("Invalid input! Please enter a valid integer.")
        return
   
read_integer()
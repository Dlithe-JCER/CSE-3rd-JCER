# Exception Example -2
n=int(input('Enter A number'))

# Handling ValueError :
try:
    n = int(input('Enter a number: '))
    print('Value of n:', n)
except ValueError:
    print('Invalid input.')


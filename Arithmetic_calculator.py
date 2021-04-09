# This calculator performs addition, Subtraction, Multiplication, Division, Modulus type of operations on integer as well as real values.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
def modulus(x,y):
    return x % y
def to_power(x):
    def calc_power(n):
        return n**x
    return  calc_power

print("-------------------- Select operation -----------------------")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Modulus")
print("6.Calculate power of a number")
while True:

    choice = input("Enter choice(1/2/3/4/5/6): ")

    if choice in ('1', '2', '3', '4','5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    if choice == '1':
       print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
       print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
       print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
           print(num1, "/", num2, "=", divide(num1, num2))
    elif choice == '5':
           print(num1, "%", num2, "=", modulus(num1, num2))
    elif choice == '6':
          n = int(input('Enter a number : '))
          x = int(input('Enter power--> (2/3/4...) : '))
          calculate = to_power(x)
          print(f'{n} ^ {x} is: {calculate(n)}')
    else:
       print("Invalid Input")

    
"""
-------------------- Select operation -----------------------
1.Add
2.Subtract
3.Multiply
4.Divide
5.Modulus
6.Calculate power of a number

Enter choice(1/2/3/4/5/6): 1
Enter first number: 89
Enter second number: 45
89.0 + 45.0 = 134.0      

Enter choice(1/2/3/4/5/6): 3
Enter first number: 3
Enter second number: 2
3.0 * 2.0 = 6.0

Enter choice(1/2/3/4/5/6): 6
Enter a number : 8
Enter power--> (2/3/4...) : 3
8 ^ 3 is: 512
Enter choice(1/2/3/4/5/6): 

"""

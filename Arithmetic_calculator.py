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

print("-------------------- Select operation -----------------------")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:

    choice = input("Enter choice(1/2/3/4/5): ")

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

    else:
       print("Invalid Input")
    
"""
-------------------- Select operation -----------------------
1.Add
2.Subtract
3.Multiply
4.Divide

Enter choice(1/2/3/4/5): 1
Enter first number: 45
Enter second number: 78
45.0 + 78.0 = 123.0

Enter choice(1/2/3/4/5): 4
Enter first number: 55
Enter second number: 5
55.0 / 5.0 = 11.0

Enter choice(1/2/3/4/5): 

"""

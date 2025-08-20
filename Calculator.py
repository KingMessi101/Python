def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def main():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Multiplication")

    choice = input("Enter your choice (1 or 2): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = add_numbers(num1, num2)
        print("Result of addition:", result)
    elif choice == '2':
        result = multiply_numbers(num1, num2)
        print("Result of multiplication:", result)
    else:
        print("Invalid choice. Please select 1 or 2.")

main()
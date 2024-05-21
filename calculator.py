def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

def calculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print("Choose operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            operation_choice = input("Enter operation number: ")

            if operation_choice == '1':
                print("Result:", add(num1, num2))
            elif operation_choice == '2':
                print("Result:", subtract(num1, num2))
            elif operation_choice == '3':
                print("Result:", multiply(num1, num2))
            elif operation_choice == '4':
                print("Result:", divide(num1, num2))
            else:
                print("Invalid operation number! Please choose a number from 1 to 4.")

            another_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if another_calculation.lower() != 'yes':
                print("Goodbye!")
                break
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    calculator()

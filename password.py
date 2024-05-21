import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        while True:
            print("\nMENU:")
            print("1. Generate Password")
            print("2. Exit")
            choice = input("Enter your choice (1/2): ")
            
            if choice == '1':
                length = int(input("Enter the desired length of the password: "))
                if length <= 0:
                    print("Invalid length! Please enter a positive integer.")
                    continue
                password = generate_password(length)
                print("Generated Password:", password)
            elif choice == '2':
                print("Exiting the password generator program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
    except ValueError:
        print("Invalid input! Please enter valid integers.")

if __name__ == "__main__":
    main()

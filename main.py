import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    characters = ''
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
        
    if not characters:
        raise ValueError("At least one character type must be selected.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password_to_file(password, filename):
    with open(filename, 'w') as file:
        file.write(password)

if __name__ == '__main__':
    print("Welcome to the Random Password Generator!")
    try:
        length = int(input("Enter the length of the password: "))
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
        print("Generated Password:", password)

        save_to_file = input("Do you want to save this password to a file? (y/n): ").lower() == 'y'
        if save_to_file:
            filename = input("Enter the filename: ")
            save_password_to_file(password, filename)
            print(f"Password has been saved to {filename}")
    except ValueError as e:
        print("Error:", e)

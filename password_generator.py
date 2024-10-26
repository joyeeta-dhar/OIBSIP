import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    # Create a pool of characters based on user preferences
    characters = ''
    if use_letters:
        characters += string.ascii_letters  # Includes both uppercase and lowercase letters
    if use_numbers:
        characters += string.digits          # Includes numbers 0-9
    if use_symbols:
        characters += string.punctuation     # Includes special symbols

    if not characters:
        raise ValueError("At least one character type must be selected.")

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired password length: "))
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    try:
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

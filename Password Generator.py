import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    """Generate a random password based on user-defined criteria."""
    character_set = ""
    
    if use_letters:
        character_set += string.ascii_letters  # a-z, A-Z
    if use_numbers:
        character_set += string.digits  # 0-9
    if use_symbols:
        character_set += string.punctuation  # !@#$%^&*() etc.
    
    if not character_set:
        print("You must select at least one character type.")
        return None
    
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def get_user_preferences():
    """Prompt user for password preferences and validate input."""
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Please enter a positive integer for length.")
                continue
            use_letters = input("Include letters? (yes/no): ").strip().lower() == 'yes'
            use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
            use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'
            return length, use_letters, use_numbers, use_symbols
        except ValueError:
            print("Invalid input. Please enter a valid number for length.")

if __name__ == "__main__":
    print("Welcome to the Random Password Generator!")
    length, use_letters, use_numbers, use_symbols = get_user_preferences()
    password = generate_password(length, use_letters, use_numbers, use_symbols)
    if password:
        print(f"Your generated password is: {password}")

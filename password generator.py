import random
import string

def generate_password(length=12):
    """Generate a random password with letters, digits, and special characters."""
    
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Create a pool of characters
    all_characters = lowercase + uppercase + digits + special_chars

    # Ensure at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest of the password length with random choices from all characters
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle the password list to randomize character positions
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)

# Main program
if __name__ == "__main__":
    print("Password Generator")
    length = int(input("Enter the desired password length (minimum 8): "))

    # Check minimum length requirement
    if length < 8:
        print("Error: Password length must be at least 8 characters.")
    else:
        password = generate_password(length)
        print(f"Generated password: {password}")
    
import math

def calculate_entropy(password):
    """
    Calculates the entropy of a password in bits.
    """
    # Define the character sets and their sizes
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special = "!@#$%^&*()-_+=~`[]{}|:;\"'<,>.?/\\"

    # Determine the character set size based on the characters present in the password
    char_set_size = 0
    if any(c in lower for c in password):
        char_set_size += len(lower)
    if any(c in upper for c in password):
        char_set_size += len(upper)
    if any(c in digits for c in password):
        char_set_size += len(digits)
    if any(c in special for c in password):
        char_set_size += len(special)

    # Handle the case of an empty password to avoid errors
    if char_set_size == 0:
        return 0

    password_length = len(password)
    entropy = password_length * math.log2(char_set_size)

    return entropy

def main():
    """
    Main function to run the password evaluator.
    """
    password = input("Enter a password to check its strength: ")
    entropy_bits = calculate_entropy(password)

    print(f"\nPassword: {password}")
    print(f"Password length: {len(password)}")
    print(f"Entropy: {entropy_bits:.2f} bits")

    # We can add more logic here to provide a 'strength' rating.
    if entropy_bits < 28:
        strength = "Very Weak"
    elif entropy_bits < 36:
        strength = "Weak"
    elif entropy_bits < 60:
        strength = "Reasonable"
    elif entropy_bits < 128:
        strength = "Strong"
    else:
        strength = "Very Strong"

    print(f"Strength Rating: {strength}")
    print("--------------------------------------------------")

if __name__ == "__main__":
    main()
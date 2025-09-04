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

def format_time(seconds):
    """
    Converts a large number of seconds into a more readable format (e.g., years, days).
    """
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        minutes = seconds / 60
        return f"{minutes:.2f} minutes"
    elif seconds < 86400:
        hours = seconds / 3600
        return f"{hours:.2f} hours"
    elif seconds < 31536000:
        days = seconds / 86400
        return f"{days:.2f} days"
    else:
        years = seconds / 31536000
        return f"{years:.2f} years"

def main():
    """
    Main function to run the password evaluator.
    """
    password = input("Enter a password to check its strength: ")
    entropy_bits = calculate_entropy(password)

    print(f"\nPassword: {password}")
    print(f"Password length: {len(password)}")
    print(f"Entropy: {entropy_bits:.2f} bits")

    # Cracking speeds in guesses per second
    slow_speed = 10**8  # 100 million guesses/sec (CPU-based)
    fast_speed = 10**12 # 1 trillion guesses/sec (GPU-based)

    # Calculate and format the estimated crack times
    if entropy_bits > 0:
        slow_crack_time = (2**entropy_bits) / slow_speed
        fast_crack_time = (2**entropy_bits) / fast_speed
        
        slow_crack_time_formatted = format_time(slow_crack_time)
        fast_crack_time_formatted = format_time(fast_crack_time)
        
        print(f"Estimated crack time (CPU): {slow_crack_time_formatted}")
        print(f"Estimated crack time (GPU): {fast_crack_time_formatted}")
    else:
        print("Estimated crack time: N/A (password is empty)")

    # Provide a strength rating based on entropy
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
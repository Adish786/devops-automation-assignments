import re  # Importing regular expression module for pattern matching

def check_password_strength(password):
    """
    Check if the given password meets the defined strength criteria:
    - At least 8 characters long
    - Contains both uppercase and lowercase letters
    - Contains at least one digit
    - Contains at least one special character
    """
    
    # Check for minimum length
    if len(password) < 8:
        return False

    # Check for at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return False

    # Check for at least one lowercase letter
    if not re.search(r"[a-z]", password):
        return False

    # Check for at least one digit
    if not re.search(r"\d", password):
        return False

    # Check for at least one special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False

    # If all conditions are satisfied, return True
    return True

if __name__ == "__main__":
    # Prompt the user to enter a password
    user_password = input("Enter your password: ")
    
    # Validate password strength and provide feedback
    if check_password_strength(user_password):
        print("✅ Strong password.")
    else:
        print("❌ Weak password. Try again with at least 8 characters, "
              "uppercase, lowercase, number, and special character.")

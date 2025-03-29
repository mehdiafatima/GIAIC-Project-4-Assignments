import hashlib

# Provided function to hash a password
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# Login function
def login(email: str, password_to_check: str, stored_logins: dict) -> bool:
    # Step 1: Hash the provided password
    hashed_password = hash_password(password_to_check)
    
    # Step 2: Check if the hashed password matches the stored hash for the email
    return stored_logins.get(email) == hashed_password

# Example usage:
if __name__ == "__main__":
    # Example stored logins (email: hashed_password)
    stored_logins = {
        "user1@example.com": hash_password("mypassword123"),
        "use78@example.com": hash_password("securepass456"),
    }
    
    # Login attempts
    print(login("user1@example.com", "mypassword123", stored_logins))  # True
    print(login("use78@example.com", "wrongpassword", stored_logins))  # False
    print(login("unknown@example.com", "somepassword", stored_logins))  # False

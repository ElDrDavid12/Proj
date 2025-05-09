import hashlib

# Define the target password (you can hash it first, but for simplicity, we use 'hello')
correct_password = "keNCEntIStELAND"

# Hash the correct password using SHA-256 (or any hashing algorithm you prefer)
hashed_password = hashlib.sha256(correct_password.encode()).hexdigest()

# Read the dictionary file (file.txt) with possible passwords
with open("/home/david/Projects/python/passwords.txt", "r") as file:
    for line in file:
        # Clean up the line and hash the current password
        password = line.strip()
        hashed_attempt = hashlib.sha256(password.encode()).hexdigest()
        
        # Compare the hashed password with the target hashed password
        if hashed_attempt == hashed_password:
            print(f"Password found: {password}")
            break
    else:
        print("Password not found.")

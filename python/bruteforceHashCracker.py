import hashlib
import itertools
import string
import concurrent.futures
import time

# Function to attempt cracking the hash using brute-force
def brute_force_crack_worker(target_hash, charset, length):
    # Generate all combinations of the given length
    for combination in itertools.product(charset, repeat=length):
        password = ''.join(combination)  # Join the tuple into a string
        
        # Hash the password using SHA-256
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        # Check if the hash matches the target
        if hashed_password == target_hash:
            return password  # Return the found password
    return None  # Return None if no password is found

def brute_force_crack(target_hash, max_length=4, num_threads=4):
    # Define the character set (lowercase, uppercase, digits)
    charset = string.ascii_letters + string.digits
    
    # Start timer for performance measurement
    start_time = time.time()
    
    # Using ThreadPoolExecutor for parallel processing
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        
        # Try all combinations of lengths from 1 to max_length
        for length in range(1, max_length + 1):
            # Submit each worker task to process different lengths in parallel
            futures.append(executor.submit(brute_force_crack_worker, target_hash, charset, length))
        
        # Wait for the first result that matches
        for future in concurrent.futures.as_completed(futures):
            cracked_password = future.result()
            if cracked_password:
                print(f"Password cracked: {cracked_password}")
                print(f"Time taken: {time.time() - start_time:.2f} seconds")
                return cracked_password
        
    # If no password is found
    print(f"Password not found within the given length.")
    print(f"Time taken: {time.time() - start_time:.2f} seconds")
    return None

# Example usage
target_hash = 'a61a438e49e3a62c8dd896237f288e986a554e4a09cd4197cd67ba51fd18cefb'  # Example target hash
max_length = 6  # Maximum password length to try (adjustable)

cracked_password = brute_force_crack(target_hash, max_length)

if not cracked_password:
    print("Password not found.")

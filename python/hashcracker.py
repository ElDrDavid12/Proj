import hashlib

def crack_hash(target_hash, wordlist, hash_algorithm='md5'):
    try:
        # Select hashing function dynamically
        hash_function = getattr(hashlib, hash_algorithm)
    except AttributeError:
        print(f"Error: The hash algorithm '{hash_algorithm}' is not supported.")
        return None

    try:
        with open(wordlist, 'r', encoding='utf-8') as file:
            for line in file:
                password = line.rstrip()  # Using rstrip to avoid unnecessary whitespace removal
                hashed_password = hash_function(password.encode()).hexdigest()
                if hashed_password == target_hash:
                    return password
        return None
    except FileNotFoundError:
        print(f"Error: The file '{wordlist}' was not found.")
        return None
    except IOError:
        print(f"Error: Could not read the file '{wordlist}'.")
        return None

# Example usage
target_hash = 'a61a438e49e3a62c8dd896237f288e986a554e4a09cd4197cd67ba51fd18cefb'  # Hash for 'keNCEntIStELAND'
wordlist = '/home/david/Projects/python/passwords.txt'

# You can specify the hash algorithm if needed (default is 'md5')
cracked_password = crack_hash(target_hash, wordlist, hash_algorithm='sha256')

if cracked_password:
    print(f"Password cracked: {cracked_password}")
else:
    print("Password not found in wordlist.")

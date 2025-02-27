import hashlib

def generate_hash(word):
    hash_obj = hashlib.sha256(word.encode())  # Encode the word and generate the hash
    return hash_obj.hexdigest()  # Return the hash in hexadecimal format

word = "security"
hash_result = generate_hash(word)
print(f"SHA-256: {hash_result}")

# This program will generate the hash value of the word "security" using the SHA-256 algorithm.
# The hash value will be printed in hexadecimal format.
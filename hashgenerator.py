import hashlib

# Supported hash algorithms
hash_algorithms = {
    'md5': hashlib.md5,
    'sha1': hashlib.sha1,
    'sha256': hashlib.sha256,
}

# Function to generate the hash for a given word and algorithm
def generate_hash(word, algorithm_name):
    algorithm = hash_algorithms.get(algorithm_name.lower(), hashlib.sha256)
    hash_obj = algorithm(word.encode())  # Encode the word and generate the hash
    return hash_obj.hexdigest()  # Return the hash in hexadecimal format

# Main function
def main():
    word = input("Enter the word to generate the hash: ").strip()
    algorithm_name = input("Enter the hash algorithm (md5, sha1, sha256): ").strip().lower()

    if not word:
        print("Please enter a valid word.")
        return

    # Generate and display the hash for the selected algorithm
    hash_result = generate_hash(word, algorithm_name)
    print(f"{algorithm_name.upper()} Hash: {hash_result}")

if __name__ == '__main__':
    main()

import hashlib
import multiprocessing
from multiprocessing import Pool
import os

# Supported hash algorithms
hash_algorithms = {
    'md5': hashlib.md5,
    'sha1': hashlib.sha1,
    'sha256': hashlib.sha256,
}

# Function to crack the hash
def crack_hash(password, hash_file, algorithm):
    hash_calculated = algorithm(password.encode()).hexdigest()
    if hash_calculated == hash_file:
        return password
    return None

# Function to process the dictionary and attempt to crack the hash
def process_dictionary(dic_file, hash_file, algorithm_name):
    # Load the dictionary
    with open(dic_file, 'r') as file:
        dic = [line.strip() for line in file]

    # Get the selected hashing algorithm
    algorithm = hash_algorithms.get(algorithm_name.lower(), hashlib.sha256)

    # Create a pool of workers for parallel processing
    with Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.starmap(crack_hash, [(password, hash_file, algorithm) for password in dic])

    # Find the password that matches
    for result in results:
        if result:
            print(f'Password found: {result}')
            break
    else:
        print('Password not found.')

# Main function
def main():
    hash_file = '5d2d3ceb7abe552344276d47d36a8175b7aeb250a9bf0bf00e850cd23ecf2e43'  # Example hash (SHA-256)
    dic_file = input('Enter the dictionary file: ')  # Path to the dictionary file, especifying the file name (dictionary.txt for example)
    algorithm_name = input('Enter the hash algorithm (md5, sha1, sha256): ').strip().lower()

    if not os.path.exists(dic_file):
        print('The dictionary file does not exist.')
        return

    # Start the process to crack the hash
    process_dictionary(dic_file, hash_file, algorithm_name)

if __name__ == '__main__':
    main()

import hashlib

hash_file = 'd41d8cd98f00b204e9800998ecf8427ed41d8cd98f00b204e9800998ecf8427e'

dic_file = input('Enter the dictionary file: ')

with open(dic_file, 'r') as file:

    dic = [line.strip() for line in file]

    for password in dic:

        hash_calculated = hashlib.sha256(password.encode()).hexdigest()

        if hash_calculated == hash_file:

            print(f'Password found: {password}')

            break
        else:
            print('Password not found')

# This program will read the dictionary file and compare the hash value with the hash value in the file. If the hash value matches, it will print the password.
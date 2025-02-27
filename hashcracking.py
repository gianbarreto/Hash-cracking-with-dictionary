import hashlib

hash_file = '5d2d3ceb7abe552344276d47d36a8175b7aeb250a9bf0bf00e850cd23ecf2e43'

dic_file = input('Enter the dictionary file: ') # Enter the dictionary file directory, with the name of the file.

with open(dic_file, 'r') as file:

    dic = [line.strip() for line in file]

    for password in dic:

        hash_calculated = hashlib.sha256(password.encode()).hexdigest()

        if hash_calculated == hash_file:

            print('Password found: ' + password)

            break
        else:
            print('Password not found')

# This program will read the dictionary file and compare the hash value with the hash value in the file. If the hash value matches, it will print the password.
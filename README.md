# Hash Cracking with Dictionary

## Objective  
The **Hash Cracking with Dictionary** project was developed to test the security of hashed passwords by attempting to crack them using a dictionary attack. This tool helps users understand the importance of strong password hashing techniques and highlights the vulnerabilities of weak or commonly used passwords.

## Skills Learned  
- Understanding of **hashing algorithms** (MD5, SHA-1, SHA-256).  
- Using **Python's hashlib library** to generate and compare hashes.  
- Implementing **dictionary attacks** to crack hashed passwords.  
- Reading and processing **wordlists** efficiently.  
- Enhancing awareness of **password security best practices**.  
- Optimizing the cracking process with **multiprocessing** and **distributed mode**.

## Tools Used  
- **Python** – Core language.  
- **Hashlib Library** – Used for generating and verifying hashes.  
- **Multiprocessing** – For optimizing the cracking process across multiple CPU cores.  
- **Distributed Mode** – For cracking hashes across multiple machines.  
- **Wordlists** (e.g., `dictionary.txt`) – To attempt cracking known hashes.

## How to use

1. First you have to create a dictionary, for example dictionary.txt, which contains the words you want to test as a password.
2. Then you have to generate a hash, with the hashgenerator.py, which is very self explanatory.
3. With that hash you can paste it in the hashcracking.py program, in the line where it says hash_file = ' '.
4. Now you can run the program, especyfing the path of the file with its name (for example: C:\Users\Admin\Desktop\Hash-cracking-with-dictionary\dictionary.txt) and let the program do the rest.

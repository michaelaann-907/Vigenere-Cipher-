"""
Project Name: File Encryption Using Vigenere Cipher 
Project Description: Write a program that can encrypt/decrypt an HTML file using Vigenere cipher. Note that
this instruction is a simplified version of what we discussed in the class. NO need to
encrypt only the human readable parts of the HTML. Instead, encrypt the entire file.
Programmer: Michaela Pierce
UNCW, CSC 592 - Introduction to Cryptography
Relative Code by: Pratik Somwanshi, 
                  url: https://www.geeksforgeeks.org/vigenere-cipher/
"""

import random
import os

# 1. Random Key Generator
# Generates a random key of specified length and saves it to a file
def generate_key(key_size):
    key = []  # Initialize an empty list to hold the key characters
    for i in range(key_size):
        # Generate a random uppercase letter and append to the key list
        key.append(chr(random.randrange(26) + ord('A')))
    # Write the generated key to a file named 'key_file.txt'
    with open("key_file.txt", "w") as key_file:
        key_file.write("".join(key))  # Convert list to string and write to file
    return "".join(key)  # Return the generated key as a string

# 2. Encryption
# Encrypts the content of a file using the Vigenere cipher
def encrypt(file_content, key):
    cipher_text = []  # Initialize an empty list to hold the encrypted text
    key_length = len(key)
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Define the alphabet for reference
    for i in range(len(file_content)):
        char = file_content[i]
        if char.isalpha():
            key_char = key[i % key_length]
            shift = alpha.index(key_char.upper())
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            # Calculate the encrypted character using the Vigenere cipher formula
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            cipher_text.append(encrypted_char)
        else:
            cipher_text.append(char)  # Keep non-alphabetical characters unchanged

    return "".join(cipher_text)  # Return the encrypted text as a string

# 3. Decryption
# Decrypts the encrypted content using the Vigenere cipher
def decrypt(cipher_text, key):
    plain_text = []  # Initialize an empty list to hold the decrypted text
    key_length = len(key)
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Define the alphabet for reference
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            shift = alpha.index(key_char.upper())
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            # Calculate the decrypted character using the Vigenere cipher formula
            decrypted_char = chr((ord(char) - base - shift + 26) % 26 + base)
            plain_text.append(decrypted_char)
        else:
            plain_text.append(char)  # Keep non-alphabetical characters unchanged

    return "".join(plain_text)  # Return the decrypted text as a string

# Driver code
if __name__ == "__main__":
    # 1a. Ask the user to input the desired key length
    key_size = int(input("Please enter the key length: "))
    # 1b. Generate a random key of the specified length and save it to a file
    key = generate_key(key_size)

    # 2a. Ask the user to input the path to the file they want to encrypt
    input_file_path = input("Enter the path to the file you want to encrypt (e.g., 'C:\\Users\\micha\\Desktop\\test.txt'): ")
    with open(input_file_path, "r") as file:
        file_content = file.read()  # Read the content of the file

    # Encrypt the file content using the generated key
    cipher_text = encrypt(file_content, key)

    # 2b. Ask the user to specify the output filename for the encrypted file
    enc_file_name = input("Enter the output filename for the encrypted file (e.g., 'C:\\Users\\micha\\Desktop\\test_enc.txt'): ")
    with open(enc_file_name, "w") as enc_file:
        enc_file.write(cipher_text)  # Save the encrypted text to the specified file
    print("The encrypted file is saved as:", enc_file_name)

    # 3a. Ask the user to specify the output filename for the decrypted file
    dec_file_name = input("Enter the output filename for the decrypted file (e.g., 'C:\\Users\\micha\\Desktop\\test_dec.txt'): ")
    # Decrypt the encrypted text using the same key
    plain_text = decrypt(cipher_text, key)

    # 3b. Save the decrypted text to the specified file
    with open(dec_file_name, "w") as dec_file:
        dec_file.write(plain_text)
    print("The decrypted file is saved as:", dec_file_name)

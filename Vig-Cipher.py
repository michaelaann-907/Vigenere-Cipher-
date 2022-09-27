"""
Project Name: File Encryption Using Vigenere Cipher 
Project Description: Write a program that can encrypt/decrypt an HTML file using Vigenere cipher. Note that
this instruction is a simplified version of what we discussed in the class. NO need to
encrypt only the human readable parts of the HTML. Instead, encrypt the entire file.
Programmer: Michaela Pierce
UNCW, CSC 592 - Introduction to Cryptography
Relative Code by: Pratik Somwanshi , url: https://www.geeksforgeeks.org/vigenere-cipher/
"""

# Python code to implement
# Vigenere Cipher

import random 

# 1. Random Key Generator 
def generate_key(key_size):
    key = []
    for i in range(key_size):
        key.append(chr(random.randrange(26)+ord('A')))
    return ("".join(key))


# 2. Encryption
def encrypt (string, key):
    cipher_text = []

    for i in range (len(string)):
        x= (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append((string[i]))
        cipher_text.append(chr(x))
    return("".join(cipher_text))


# 3. Decryption
def decrypt (cipher_text, key):
    plain_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        plain_text.append(chr(x))
    return("" . join(plain_text))
     

#Driver code
if __name__ == "__main__":
    #main
    #open file in read mode 
    file_path = open("test.html", "r")

    #read file to string
    string = file_path.read()
    file_path.close()

    #ask user for key size 
    key_size = (int(input("Please enter a number for the key size:")))
    
    #generate key size 
    key = generate_key (key_size)
    
    #encryption
    cipher_text = encrypt(string, key)
    print(cipher_text)

    #decryption
    plain_text = decrypt(cipher_text, key)
    print(plain_text)
    
    
   


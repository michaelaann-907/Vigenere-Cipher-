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
def generate_key(key_size):
    key = []
    for i in range(key_size):
        key.append(chr(random.randrange(26)+ord('A')))
    #write key to file 
    key_file = open("key_file.txt" , "w")
    key_file.write("".join(key))
    key_file.close()
    return ("".join(key))

# 2. Encryption
def encrypt(file_path, key):
    cipher_text = []
    for c in range(0,len(file_path)):
        x = (ord(file_path[c])) + ord(key[c])% 26
        x += ord('A')
    return("".join(cipher_text))

    if file_path[c].isupper():
            cipher_text.append(chr(x))
    elif file_path[c].islower():
            cipher_text.append(chr(x).lower())
    
    cipher_text.append(chr(x))
    file_path = ("".join(cipher_text))


def decrypt(cipher_text, key):
    key = ""
    plain_text = []
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for c in range(len(cipher_text)):
        if alpha.find(cipher_text[c].upper()) == -1:
            plain_text.append(cipher_text[c])
            continue
        x = (ord(cipher_text[c].upper()) -
             ord(key[c]) + 26) % 26
        x += ord('A')

        if cipher_text[c].isupper():
            plain_text.append(chr(x))
        elif cipher_text[c].islower():
            plain_text.append(chr(x).lower())



#Driver code 
if __name__=="__main__":
    #main
    # 1a. Input: key length n / ask user for key length
    key_size = (int(input("Please enter a #:")))
    # 1b. Output: random text of length n / generate key size 
    key_file = generate_key(key_size)
    
    # 2a. Input: path to a txt file and the file that has the key
    #open file in read mode 
    file_path =  open (r'C:\Users\micha\Desktop\test.txt') 
    file_path = file_path.read()
    cipher_text= encrypt(file_path, key_file)
    # 2b. Output: encrypted txt file (add_enc to the end of the new filename) 
    print("Ciphertext:" , cipher_text)
    enc_file = r'C:\Users\micha\Desktop\test_enc.txt'
    #rename the file adding _enc to filename 
    os.rename (file_path , enc_file)
    print("The encrypted file name is", enc_file)

    # 3a. Input: path to the encrypted txt file and the file with key
    #enc_file is the path for the encrypted txt file 
    plain_text = decrypt (enc_file , key_file)
    # 3b. Output: decrypted html file (add _dec to end of filename)
    print("Plaintext: ", plain_text)
    dec_file = r'C:\Users\micha\Desktop\test_dec.txt'
    #rename the file 
    os.rename (enc_file, dec_file)
    print("The decrypted file name is:" , dec_file)


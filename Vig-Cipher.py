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
import os

# 1. Random Key Generator 
def generate_key(key_size):
    key = []
    for i in range (key_size):
        key.append(chr(random.randrange(26) + ord('A')))
        keyFile = open("key_file.txt" , "w") 
        keyFile.write("".join(key))
        keyFile.close()
    return
    
    
def file_string (file_path):
    with open (file_path , "r") as text_file:
        string_file = text_file.read()
    return string_file

def expand_key (string, key_size):
    string = "test.html"
    return(string * (int(key_size/len(string))+1))[:key_size]

def keyTXT_path(key_file):  #
    key = ""
    with open ("key_file.txt", "r") as key_file:
        lines = key_file.readlines ()
    with open ("key_file.txt" , "w") as key_file:
        for line in lines:
            key += line
def plainTXT_path (plain_text):
    with open (plain_text, "r" ) as html_file:
        lines = html_file.readlines()
        for line in lines:
            plain_text += line
            
# 2. Encryption
def encrypt (string, key):
    cipher_text = []
    plain_text = "" 

    key = keyTXT_path(key_path)

    plain_text = plainTXT_path (string)

    expandK = expand_key(key,len(string))


    alphabet_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range (len(plain_text)):
        if alphabet_string.find (plain_text[i].upper()) == -1:
            cipher_text.append((plain_text[i]))
            continue 
        x = (ord(plain_text[i].upper()) + ord(expandK [i])) % 26
        x += ord('A')

        if plain_text[i].isupper():
            cipher_text.append(chr(x))
        elif plain_text[i].islower():
            cipher_text.append(chr(x).lower())

 #save new encrypted file and change file name 
    html_file = open(os.path.basename(plain_text_file).replace(".html", "_enc.html") , "x")
    html_file.close()

    enc_file = os.path.basename(plain_text_file).replace(".html" , "_enc.html")

    lines = ("".join(cipher_text))

    
    with open(enc_file , "w") as f:
        for line in lines:
            f.write(line)
    print(enc_file)
    
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
    #main
    # 1a. Input: key length n / ask user for key length
    key_size = 7
    
    # 1b. Output: random text of length n / generate key size 
    key = generate_key (key_size)
    print(key)

    # 2a. Input: path to a html file and the file that has the key
    #open file in read mode 
   
    #read file to string
    plain_text_file = ("test.html")
    string = plain_text_file
    
    # 2b. Output: encrypted html file (add_enc to the end of the new filename)
    encryption = encrypt("test.html", key)
    #print(encryption)

    # 3a. Input: path to the encrypted html file and the file
    # that has the key 

    # 3b. Output: decrypted html file (add _dec to the end of
    # the new filename )
    #decryption
    #plain_text = decrypt(cipher_text, key)
    #print(plain_text)
    
    
   


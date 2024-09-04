# Vigenere Cipher
This project provides a tool for encrypting and decrypting files using the Vigenere cipher. The entire content of a file, including HTML or text, is encrypted.


## Features

- Generate a random encryption key.
- Encrypt and decrypt files using the Vigenere cipher.
- Save and manage encryption keys.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/vigenere-cipher.git
   ```


2. Navigate to the project directory:
   ```bash
   cd vigenere-cipher
   ```

## Usage

1. Run the script:
   ```bash
   python vigenere_cipher.py
   ```

2. Follow these prompts:
   - Enter key length to generate a random key.
   - Provide the path to the file you want to encrypt.
   - Specify the output filename for the encrypted file.
   - Provide the path to the encrypted file for decryption.
   - Specify the output filename for the decrypted file.

### Example

```plaintext
Please enter the key length: 10
Enter the path to the file you want to encrypt: C:\\Users\\micha\\Desktop\\sample.txt
Enter the output filename for the encrypted file: C:\\Users\\micha\\Desktop\\sample_enc.txt
Enter the output filename for the decrypted file: C:\\Users\\micha\\Desktop\\sample_dec.txt
```

## Key File

- **File Name**: `key_file.txt`
- **Content**: Contains the randomly generated encryption key.
- **Location**: Saved in the same directory as the script.

## How It Works

1. **Generate Key**: Create a random key and save it to `key_file.txt`.
2. **Encrypt File**: Encrypt the file content using the generated key.
3. **Decrypt File**: Decrypt the encrypted file using the same key.

## Code Overview

- **`generate_key(key_size)`**: Generates and saves a random key.
- **`encrypt(file_content, key)`**: Encrypts content using the key.
- **`decrypt(cipher_text, key)`**: Decrypts content using the key.

## Acknowledgements
- **Relative Code by**: Pratik Somwanshi ([GeeksforGeeks](https://www.geeksforgeeks.org/vigenere-cipher/))

## License

MIT License. See the [LICENSE](LICENSE) file for details.


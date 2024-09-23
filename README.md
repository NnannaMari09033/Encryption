# Caesar Cipher Encryption

## Table of Contents
- [Introduction](#introduction)
- [History of Encryption and Caesar Cipher](#history-of-encryption-and-caesar-cipher)
- [Purpose of This Project](#purpose-of-this-project)
- [How the Caesar Cipher Works](#how-the-caesar-cipher-works)
- [Code Explanation](#code-explanation)
- [Usage](#usage)
- [Conclusion](#conclusion)

## Introduction
This project demonstrates a simple implementation of the Caesar Cipher, one of the oldest encryption techniques. The Caesar Cipher is a substitution cipher that shifts the letters of the alphabet by a specified number of positions to create an encrypted message.

## History of Encryption and Caesar Cipher
Encryption has been used throughout history to protect sensitive information. One of the earliest known encryption techniques is the **Caesar Cipher**, named after **Julius Caesar**, who used it to securely communicate with his military generals.

The Caesar Cipher works by shifting the alphabet by a fixed number of positions. For example, with a shift of 3, the letter 'A' becomes 'D', 'B' becomes 'E', and so on. This method was simple but effective during its time.

## Purpose of This Project
The goal of this project is to:
1. Provide a basic understanding of how encryption works.
2. Demonstrate the implementation of the Caesar Cipher.
3. Explore the concepts of encryption and decryption using Python.

## How the Caesar Cipher Works
The Caesar Cipher uses a simple algorithm to encrypt and decrypt messages:
- **Encryption**: Each letter in the plaintext is shifted by a certain number of positions (the "key") in the alphabet. If the shift exceeds the length of the alphabet, it wraps around from the beginning.
- **Decryption**: The reverse of encryption, where the letters are shifted backward by the same number of positions to retrieve the original message.

For example, if the key is 3:
- Plaintext: `abc`
- Ciphertext: `def`

## Code Explanation
The Python implementation of the Caesar Cipher includes two main functions: `encrypt` and `decrypt`.

### 1. Encryption Function
```python
def encrypt(plaintext, key):
    cipher_text = ""
    for letter in plaintext:
        if letter.isalpha():
            letter = letter.lower()
            index = alphabet.find(letter)
            new_index = (index + key) % num_letters
            cipher_text += alphabet[new_index]
        else:
            cipher_text += letter
    return cipher_text
Explanation:
The encrypt function takes in two parameters: plaintext (the message to be encrypted) and key (the shift value).
Each letter in the plaintext is shifted by the key and added to the ciphertext.
Non-alphabetic characters remain unchanged.
2. Decryption Function
python
def decrypt(ciphertext, key):
    plaintext = ""
    for letter in ciphertext:
        if letter.isalpha():
            letter = letter.lower()
            index = alphabet.find(letter)
            new_index = (index - key) % num_letters
            plaintext += alphabet[new_index]
        else:
            plaintext += letter
    return plaintext
Explanation:
The decrypt function reverses the encryption by shifting the letters back by the key value to retrieve the original plaintext.
Non-alphabetic characters are ignored.
Usage
You can use the program by running the following script:

python
print("Caesar cipher program\n")

user_input = input("Do you want to encrypt or decrypt? Enter 'e' for encrypt or 'd' for decrypt: ").lower()

if user_input == "e":
    print("Encryption mode activated!\n")
    key = int(input("Enter the key you want to encrypt (1 through 26): "))
    text = input("Enter the word you want to encrypt: ").lower()
    cipher_text = encrypt(text, key)
    print(f"Encrypted text: {cipher_text}")
    
elif user_input == "d":
    print("Decryption mode activated!\n")
    key = int(input("Enter the key you want to decrypt (1 through 26): "))
    text = input("Enter the word you want to decrypt: ").lower()
    plaintext = decrypt(text, key)
    print(f"Decrypted text: {plaintext}")
else:
    print("Invalid input. Please enter 'e' for encrypt or 'd' for decrypt.")
To encrypt a message, enter 'e', choose a key (shift value), and input your message.
To decrypt a message, enter 'd', provide the key, and input the encrypted message.
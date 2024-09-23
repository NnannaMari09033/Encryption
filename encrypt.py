alphabet = "abcdefghijklmnopqrstuvwxyz"
num_letters = len(alphabet)

def encrypt(plaintext, key):
    cipher_text = ""
    for letter in plaintext:
        if letter.isalpha():  # Check if it's an alphabetic character
            letter = letter.lower()
            index = alphabet.find(letter)
            if index != -1:  # Found in the alphabet
                new_index = (index + key) % num_letters
                cipher_text += alphabet[new_index]
            else:
                cipher_text += letter  # Non-alphabetic characters
        else:
            cipher_text += letter  # Spaces or non-alphabetic characters
    return cipher_text

def decrypt(ciphertext, key):
    plaintext = ""
    for letter in ciphertext:
        if letter.isalpha():  # Check if it's an alphabetic character
            letter = letter.lower()
            index = alphabet.find(letter)
            if index != -1:  # Found in the alphabet
                new_index = (index - key) % num_letters
                plaintext += alphabet[new_index]
            else:
                plaintext += letter  # Non-alphabetic characters
        else:
            plaintext += letter  # Spaces or non-alphabetic characters
    return plaintext

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
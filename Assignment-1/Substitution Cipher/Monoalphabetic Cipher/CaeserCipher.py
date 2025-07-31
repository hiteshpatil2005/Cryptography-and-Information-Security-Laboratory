plaintext = input("Enter the plaintext: ")
key = int(input("Enter the key (shift): "))

def EncryptFunct(plaintext, key):
    ciphertext = ""
    for ch in plaintext:
        if ch.isupper():
            ch = chr(((ord(ch) - ord('A') + key) % 26) + ord('A'))
        elif ch.islower():
            ch = chr(((ord(ch) - ord('a') + key) % 26) + ord('a'))
        ciphertext += ch
    return ciphertext

def DecryptFunct(ciphertext, key):
    plaintext = ""
    for ch in ciphertext:
        if ch.isupper():
            ch = chr(((ord(ch) - ord('A') - key + 26) % 26) + ord('A'))
        elif ch.islower():
            ch = chr(((ord(ch) - ord('a') - key + 26) % 26) + ord('a'))
        plaintext += ch
    return plaintext

ciphertext = EncryptFunct(plaintext, key)
print("Encrypted Ciphertext:", ciphertext)

decrypted = DecryptFunct(ciphertext, key)
print("Decrypted Plaintext:", decrypted)

plaintext = input("Enter the plaintext: ")
a = int(input("Enter the key (a): "))
b = int(input("Enter the key (b): "))

def AffineCipherEncrypt(plaintext, a, b):
    ciphertext = ""
    for ch in plaintext:
        if ch.isupper():
            ch = chr(((a * (ord(ch) - ord('A')) + b) % 26) + ord('A'))
        elif ch.islower():
            ch = chr(((a * (ord(ch) - ord('a')) + b) % 26) + ord('a'))
        ciphertext += ch
    return ciphertext

ciphertext = AffineCipherEncrypt(plaintext, a, b)
print("Ciphertext:", ciphertext)    
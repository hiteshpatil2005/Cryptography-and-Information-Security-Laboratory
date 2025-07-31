def AtbashCipherEncrypt(text):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr(ord('A') + (ord('Z') - ord(ch)))
        elif ch.islower():
            result += chr(ord('a') + (ord('z') - ord(ch)))
        else:
            result += ch 
    return result

def AtbashCipherDecrypt(text):
    decryptResult = ""
    for ch in text:
        if ch.isupper():
            decryptResult += chr(ord('A') + (ord('Z') - ord(ch)))
        elif ch.islower():
            decryptResult += chr(ord('a') + (ord('z') - ord(ch)))
        else:
            decryptResult += ch 
    return decryptResult

text = input("Enter the text for Atbash Cipher: ")

ciphered = AtbashCipherEncrypt(text)
print("Atbash Cipher Output:", ciphered)

decrypted = AtbashCipherDecrypt(ciphered)
print("Decrypted Text:", decrypted)

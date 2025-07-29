def AtbashCipher(text):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr(ord('A') + (ord('Z') - ord(ch)))
        elif ch.islower():
            result += chr(ord('a') + (ord('z') - ord(ch)))
        else:
            result += ch 
    return result

text = input("Enter the text for Atbash Cipher: ")
ciphered = AtbashCipher(text)
print("Atbash Cipher Output:", ciphered)

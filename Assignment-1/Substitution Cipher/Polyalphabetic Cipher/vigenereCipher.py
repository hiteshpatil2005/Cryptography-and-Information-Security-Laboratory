plaintext = input("Enter the plaintext : ")
keyword = input("Enter the Keyword : ")

cipherText = ""

for ch in range(len(plaintext)):
    if plaintext[ch].isupper():
        index = ord(plaintext[ch]) - ord('A') + ord(keyword[ch % len(keyword)].upper()) - ord('A')
        index = index % 26
        cipherText += keyword[index].upper()

    elif plaintext[ch].islower():
        index = ord(plaintext[ch]) - ord('a') + ord(keyword[ch % len(keyword)].lower()) - ord('a')
        index = index % 26
        cipherText += keyword[index].lower()

    else:
        cipherText += plaintext[ch]
print("Ciphertext:", cipherText)

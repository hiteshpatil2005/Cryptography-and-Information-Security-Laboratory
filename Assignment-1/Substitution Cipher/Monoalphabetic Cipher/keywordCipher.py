print("Keyword Cipher")

plaintext = input("Enter the plaintext : ")
keyword = input("Enter the keyword : ")

alphabetSeries = ''.join(dict.fromkeys(keyword + "abcdefghijklmnopqrstuvwxyz"))

cipherText = ""

for ch in plaintext:
    if ch.isupper():
        index = ord(ch) - ord('A')
        cipherText += alphabetSeries[index].upper()
    elif ch.islower():
        index = ord(ch) - ord('a')
        cipherText += alphabetSeries[index].lower()
    else:
        cipherText += ch

print("Ciphertext:", cipherText)

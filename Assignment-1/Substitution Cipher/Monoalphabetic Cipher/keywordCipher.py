# Keyword Cipher Implementation (Encryption)

def generate_keyword_key(keyword):
    keyword = keyword.upper()
    unique_keyword = ''.join(sorted(set(keyword), key=keyword.index))
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    remaining_letters = ''.join([ch for ch in alphabet if ch not in unique_keyword])
    full_key = unique_keyword + remaining_letters
    return full_key

plaintext = input("Enter the plaintext: ")

keyword = input("Enter the keyword (only letters): ")

key = generate_keyword_key(keyword)

ciphertext = []

for char in plaintext:
    if char.isalpha():
        is_upper = char.isupper()
        index = ord(char.upper()) - ord('A')
        substituted_char = key[index]
        if not is_upper:
            substituted_char = substituted_char.lower()
        ciphertext.append(substituted_char)
    else:
        ciphertext.append(char)

encrypted_text = ''.join(ciphertext)
print("Encrypted Text:", encrypted_text)
print("Hill Cipher Implementation")

def getKeyMatrix(key, n):
    keyMatrix = [[0] * n for _ in range(n)]
    k = 0
    for i in range(n):
        for j in range(n):
            keyMatrix[i][j] = ord(key[k].upper()) % 65
            k += 1
    return keyMatrix

def encrypt_block(block, keyMatrix, n):
    messageVector = [[ord(char.upper()) % 65] for char in block]
    cipherMatrix = [[0] for _ in range(n)]
    for i in range(n):
        for x in range(n):
            cipherMatrix[i][0] += keyMatrix[i][x] * messageVector[x][0]
        cipherMatrix[i][0] %= 26
    return ''.join(chr(cipherMatrix[i][0] + 65) for i in range(n))

def HillCipher(message, key, n):
    if len(key) != n * n:
        print(f"Error: Key must be exactly {n*n} characters long.")
        return

    message = message.upper().replace(" ", "")
    keyMatrix = getKeyMatrix(key, n)

    # Padding message to make it divisible by n
    while len(message) % n != 0:
        message += 'X'

    cipherText = ""
    for i in range(0, len(message), n):
        block = message[i:i + n]
        cipherText += encrypt_block(block, keyMatrix, n)

    print("Ciphertext:", cipherText)

n = int(input("Enter matrix size n (for n x n key matrix): "))
plaintext = input("Enter the plaintext: ")
key = input(f"Enter the {n*n}-letter key: ")
HillCipher(plaintext, key, n)
   

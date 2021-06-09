def encrypt(plaintext, key):
    ciphertext = ""
    for character in plaintext:
        if(character == " "):
            ciphertext+= character
        elif (character.isupper()):
            ciphertext += chr((ord(character) + key - 65) % 26 + 65)
        else:
            ciphertext = ciphertext + chr((ord(character) + key - 97) % 26 + 97)
    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ""
    for character in ciphertext:
        if(character == " "):
            plaintext+= character
        elif (character.isupper()):
            plaintext += chr((ord(character) - key - 65) % 26 + 65)
        else:
            plaintext += chr((ord(character) - key - 97) % 26 + 97)
    return plaintext


# inputtext = input("Enter text: ")
key = int(input("Enter key: "))
choice = int(input("Choice:\n Encrypt(1)\tDecrypt(2)\n"))
n =10
if(choice == 1):
    while(n!=0):
        inputtext = input("Enter text: ")
        print(encrypt(inputtext, key))
else:
    # print(decrypt(inputtext, key))
    pass

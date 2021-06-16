def encrypt(plaintext, key):
    ciphertext = ""
    for character in plaintext:   
        # ignore spaces
        if(character == " "):
            ciphertext += character
        # if character is uppercase
        elif (character.isupper()):
            ciphertext += chr((ord(character) - 65 + key) % 26 + 65)
        # if character is lowercase
        else:
            ciphertext += chr((ord(character) + key - 97) % 26 + 97)
    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ""
    for character in ciphertext:
        if(character == " "):
            plaintext += character
        elif (character.isupper()):
            plaintext += chr((ord(character) - key - 65) % 26 + 65)
        else:
            plaintext += chr((ord(character) - key - 97) % 26 + 97)
    return plaintext


inputtext = input("Enter text: ")
key = int(input("Enter key: "))
choice = int(input("Choice:\nEncrypt(1)\tDecrypt(2)\n"))
if(choice == 1):
    print(encrypt(inputtext, key))
else:
    print(decrypt(inputtext, key))

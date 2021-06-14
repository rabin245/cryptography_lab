key_keys = "abcdefghijklmnopqrstuvwxyz"
key_values = "qwertyuiopasdfghjklzxcvbnm"
key_keys = list(key_keys)
key_values = list(key_values)
# encryption_dict = {key_keys[i] : key_values[i] for i in range(len(key_keys))}
# creating dictionaries/maps for both encryption and decryption
encryption_dict = dict(zip(key_keys, key_values))
decryption_dict = dict(zip(key_values, key_keys))


def encrypt(plaintext):
    ciphertext = ""
    for char in plaintext:
        if(char.isupper()):
            char = char.lower() # if upper, convert to lower first then convert back to upper later after encryption
            ciphertext += (encryption_dict.get(char, char)).upper()
        else:
            ciphertext += encryption_dict.get(char, char)
    return ciphertext

def decrypt(ciphertext):
    plaintext = ""
    for char in ciphertext:
        if(char.isupper()):
            char = char.lower()
            plaintext += (decryption_dict.get(char, char)).upper()
        else:
            plaintext += decryption_dict.get(char, char)
    return plaintext


inputtext = input("Enter text")
choice = int(input("Choose\nEncrypt : 1\nDecrypt : 2\n"))
if(choice == 1):
    print(encrypt(inputtext))
elif(choice == 2):
    print(decrypt(inputtext))

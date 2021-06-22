import random


def getKey(length):
    key_place = [random.randint(0, 25) for i in range(length)]
    key = [chr(place+97) for place in key_place]
    print('Random key: ')
    print(''.join(key))
    return key_place

plain_text = str(input("Enter plaintext: "))
plain_text = plain_text.lower()
plain_text = plain_text.replace(" ", "")

key_place = getKey(len(plain_text))


def encrypt():
    plain_place = [(ord(char)-97) for char in plain_text]

    cipher_text = list()
    cipher_text = [(chr(((key_place[i]+plain_place[i]) % 26)+97))
                   for i in range(len(plain_place))]
    return cipher_text

def decrypt(cipher_text):
    cipher_place = [(ord(char)-97) for char in cipher_text]

    plain_text = list()
    plain_text = [(chr(((cipher_place[i]-key_place[i]) % 26)+97))
                   for i in range(len(cipher_place))]
    return plain_text
    
cipher_text=encrypt()
print("\nCipher text: ")
print(''.join(cipher_text))

plain_text=decrypt(cipher_text)
print("\nPlain text: ")
print(''.join(plain_text))

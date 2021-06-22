key = input("Enter key: ")
key = key.replace(' ', '')
key = key.lower()
key_place = [(ord(char)-97) for char in key]


result_key = []
result_key.extend(key_place)


def encrypt():
    plain_text = str(input("Enter plaintext: "))
    plain_text = plain_text.lower()
    plain_text = plain_text.replace(" ", "")

    plain_place = [(ord(char)-97) for char in plain_text]

    # copy the plaintext to result_key until length of result_key is equals to plain_text
    length_check = False
    while not length_check:
        # add the plain text to result key instead of keyword itself
        for value in plain_place:
            result_key.append(value)
            if len(result_key) == len(plain_text):
                length_check = True
                break

    cipher_text = list()
    cipher_text = [(chr(((result_key[i]+plain_place[i]) % 26)+97))
                   for i in range(len(plain_place))]

    print(''.join(cipher_text))


def decrypt():
    cipher_text = str(input("Enter ciphertext: "))
    cipher_text = cipher_text.lower()
    cipher_text = cipher_text.replace(" ", "")
    plain_text = list()

    cipher_place = [(ord(char)-97) for char in cipher_text]

    # add the decrypted letters to result_key because result_key = keyword+plaintext
    for i in range(len(cipher_text)):
        current_letter = (cipher_place[i] - result_key[i]) % 26

        if len(result_key) < len(cipher_text):
            result_key.append(current_letter)
        plain_text.append(chr(current_letter+97))

    print(''.join(plain_text))


choice = int(input("\nEnter your choice:\n1. Encrypt\n2. Decrypt\n3. Exit\n"))
if choice == 1:
    encrypt()
elif choice == 2:
    decrypt()
elif choice == 3:
    exit()
else:
    print("Choose correct choice!!!!")

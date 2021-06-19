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

    # copy the key to result_key until length of result_key is equals to plain_text
    length_check = False
    while not length_check:
        for value in key_place:
            result_key.append(value)
            if len(result_key) == len(plain_text):
                length_check = True
                break

    cipher_text = list()
    # add the letters place values of result key and plain place to get cipher_text
    cipher_text = [(chr(((result_key[i]+plain_place[i]) % 26)+97))
                   for i in range(len(plain_place))]

    print(''.join(cipher_text))


def decrypt():
    cipher_text = str(input("Enter ciphertext: "))
    cipher_text = cipher_text.lower()
    cipher_text = cipher_text.replace(" ", "")

    cipher_place = [(ord(char)-97) for char in cipher_text]
    
    length_check = False
    while not length_check:
        for value in key_place:
            result_key.append(value)
            if len(result_key) == len(cipher_text):
                length_check = True
                break

    plain_text = list()
    plain_text = [(chr(((cipher_place[i]-result_key[i]) % 26)+97))
                  for i in range(len(cipher_place))]

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

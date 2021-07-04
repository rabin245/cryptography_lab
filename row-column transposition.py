keyword = str(input("Enter the key:"))
keyword = keyword.lower()
keyword = keyword.replace(' ', '')
keyword = list(keyword)
# edbcfgh
key = list()
for letter in keyword:
    if letter not in key:
        key.append(letter)
key = [ord(letter)-97 for letter in key]


def encrypt():
    plaintext = str(input('Enter plaintext:'))
    plaintext = plaintext.lower()
    plaintext = plaintext.replace(' ', '')
    plaintext = list(plaintext)
    while(len(plaintext) % len(key) != 0):
        plaintext.append('z')
    plaintext = [plaintext[i:i+len(key)]
                 for i in range(0, len(plaintext), len(key))]
    ciphertext = list()
    temp_key = list()
    temp_key.extend(key)
    while (temp_key != []):
        min_letter = min(temp_key)
        column = key.index(min_letter)
        temp_key.remove(min_letter)
        for i in range(len(plaintext)):
            ciphertext.append(plaintext[i][column])
    print('Cipher text: ')
    print(''.join(ciphertext))


def decrypt():
    ciphertext = str(input('Enter ciphertext:'))
    ciphertext = ciphertext.lower()
    ciphertext = ciphertext.replace(' ', '')
    ciphertext = list(ciphertext)

    column_length = len(ciphertext)//len(key)
    temp = list()
    temp_key = list()
    temp = [ciphertext[i:i+column_length]
            for i in range(0, len(ciphertext), column_length)]
    print(temp)
    plaintext = [[] for row in temp]
    temp_key.extend(key)
    i = 0
    while(temp_key != []):
        min_letter = min(temp_key)
        row = key.index(min_letter)
        temp_key.remove(min_letter)
        plaintext[row] = temp[i]
        i += 1

    plaintext = [row_matrix[i]
                 for i in range(column_length) for row_matrix in plaintext]
    print(''.join(plaintext))


choice = int(input("\nEnter your choice:\n1. Encrypt\n2. Decrypt\n3. Exit\n"))
if choice == 1:
    encrypt()
elif choice == 2:
    decrypt()
elif choice == 3:
    exit()
else:
    print("Choose correct choice!!!!")

key = input("Enter key:")
key = key.replace(' ', '')
key = key.replace('j', 'i')
key = key.lower()

result = []

for character in key:
    if character not in result:  # to avoid duplicate letters
        result.append(character)

# append remaining alphabets
for i in range(97, 123):
    if chr(i) not in result:
        if (i == 105):
            result.append('i')
        elif (i == 105 or i == 106):
            pass
        else:
            result.append(chr(i))

# creating 5x5 table(matrix)
table = [result[i:i+5] for i in range(0, len(result), 5)]

# return index of the letter in the matrix


def return_index(letter):
    index = []

    for i, row_list in enumerate(table):
        for j, value in enumerate(row_list):
            if letter == value:
                index.append(i)
                index.append(j)
                return index

def encrypt():
    plain_text = str(input("Enter plaintext:"))
    plain_text = plain_text.lower()
    plain_text = plain_text.replace(" ", "")
    plain_text = plain_text.replace('j','i')

    cipher_text = list()

    for pos in range(0, len(plain_text), 2):
        if pos < len(plain_text)-1:
            # if two letters are same add x in between them
            if plain_text[pos] == plain_text[pos+1]:
                plain_text = plain_text[:pos+1]+'x'+plain_text[pos+1:]
    # if the final length of plaintext is odd, make it even
    if len(plain_text) % 2 != 0:
        plain_text = plain_text[:]+'x'

    for i in range(0, len(plain_text), 2):
        first_index = list()  # index of first letter of a pair in the table
        second_index = list()  # index of second letter of a pair in the table
        first_index = return_index(plain_text[i])
        second_index = return_index(plain_text[i+1])

        # if the letters are in the same column
        if (first_index[1] == second_index[1]):
            cipher_text.append(table[(first_index[0]+1) % 5][first_index[1]])
            cipher_text.append(table[(second_index[0]+1) % 5][second_index[1]])
        # if the letters are in the same row
        elif (first_index[0] == second_index[0]):
            cipher_text.append(table[first_index[0]][(first_index[1]+1) % 5])
            cipher_text.append(table[second_index[0]][(second_index[1]+1) % 5])
        # if the letters are in different row and column
        else:
            cipher_text.append(table[first_index[0]][second_index[1]])
            cipher_text.append(table[second_index[0]][first_index[1]])
    # print(cipher_text)
    print(''.join(cipher_text))


def decrypt():
    cipher_text = str(input("Enter ciphertext:"))
    cipher_text = cipher_text.lower()
    cipher_text = cipher_text.replace(" ", "")

    plain_text = list()

    for i in range(0, len(cipher_text), 2):
        first_index = list()  # index of first letter of a pair in the table
        second_index = list()  # index of second letter of a pair in the table
        first_index = return_index(cipher_text[i])
        second_index = return_index(cipher_text[i+1])

        # if the letters are in the same column
        if (first_index[1] == second_index[1]):
            plain_text.append(table[(first_index[0]-1) % 5][first_index[1]])
            plain_text.append(table[(second_index[0]-1) % 5][second_index[1]])
        # if the letters are in the same row
        elif (first_index[0] == second_index[0]):
            plain_text.append(table[first_index[0]][(first_index[1]-1) % 5])
            plain_text.append(table[second_index[0]][(second_index[1]-1) % 5])
        # if the letters are in different row and column
        else:
            plain_text.append(table[first_index[0]][second_index[1]])
            plain_text.append(table[second_index[0]][first_index[1]])
    # print(plain_text)
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
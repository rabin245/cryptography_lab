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
    # add bogus letter 'z' to complete the matrix
    while(len(plaintext) % len(key) != 0):
        plaintext.append('z')
    # convert list to nested list (array) with column size of len(key)
    plaintext = [plaintext[i:i+len(key)]
                 for i in range(0, len(plaintext), len(key))]
    ciphertext = list()
    temp_key = list()
    temp_key.extend(key)
    while (temp_key != []):
        min_letter = min(temp_key)
        column = key.index(min_letter)
        temp_key.remove(min_letter)
        # append the column with the index corresponding to the lowest value in the list key
        for i in range(len(plaintext)):
            ciphertext.append(plaintext[i][column])
    print('Cipher text:')
    print(''.join(ciphertext))


def decrypt():
    ciphertext = str(input('Enter ciphertext:'))
    ciphertext = ciphertext.lower()
    ciphertext = ciphertext.replace(' ', '')
    ciphertext = list(ciphertext)

    column_length = len(ciphertext)//len(key)   # to calculate the no of columns i.e rowXcolumn = len(ciphertext)
    temp = list()
    temp_key = list()
    # convert ilst to array
    temp = [ciphertext[i:i+column_length]
            for i in range(0, len(ciphertext), column_length)]
    plaintext = [[] for row in temp]
    temp_key.extend(key)
    i = 0
    
    while(temp_key != []):
        min_letter = min(temp_key)    # calculate the minimum value in key
        row = key.index(min_letter)   # get the index of the minimum value
        temp_key.remove(min_letter)   # remove the min value from the temp_key for next loop
        plaintext[row] = temp[i]      # assign the rows of temp/ciphertext matrix to its actual positions denoted by the row index
        i += 1

    #transpose and convert to list/1D array
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

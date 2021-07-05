def encrypt():
    plaintext = str(input("enter plaintext:"))
    plaintext = plaintext.lower()
    plaintext = plaintext.replace(' ', '')
    plaintext = list(plaintext)

    rails = int(input('Enter number of rails:'))
    ciphertext = list()
    # create a nested list with rows equal to number of rails
    for i in range(rails):
        ciphertext.append([])
        
    dir_down = False  # bool variable to check what the direction is
    row = 0

    for letter in plaintext:
        # if the current pointer is either at the top or bottom rail, flip the direction
        if row == 0 or row == rails-1:
            dir_down = not dir_down
        
        ciphertext[row].append(letter)

        if dir_down:
            row += 1
        else:
            row -= 1
    ciphertext = [row[i] for row in ciphertext for i in range(len(row))]
    print('Cipher text:')
    print(''.join(ciphertext))


def decrypt():
    ciphertext = str(input("enter ciphertext:"))
    ciphertext = ciphertext.lower()
    ciphertext = ciphertext.replace(' ', '')
    ciphertext = list(ciphertext)

    rails = int(input('Enter number of rails: '))
    plaintext = list()

    temp = list()
    # making an array with 'rails' rows and column equal to len(ciphertext)
    temp = [['' for i in range(len(ciphertext))] for j in range(rails)]

    dir_down = False
    row, col = 0, 0

    for letter in ciphertext:
        if row == 0 or row == rails-1:
            dir_down = not dir_down
        # assigning '*' to the place values where the plaintext letters would go in
        temp[row][col] = '*'
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1

    count = 0
    # using the previous '*' to assign letters in their respective positions
    for row in range(len(temp)):
        for i in range(len(ciphertext)):
            if(temp[row][i] == '*'):
                temp[row][i] = ciphertext[count]
                count += 1

    # traversing the array like before and appending the letters to plaintext
    dir_down = False
    row, col = 0, 0

    for i in range(len(ciphertext)):
        if row == 0 or row == rails-1:
            dir_down = not dir_down
        plaintext.append(temp[row][col])

        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    print('Cipher text:')
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

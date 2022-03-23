valid = False
while not valid:
    key = input("Enter key:")
    key = key.replace(' ', '')
    key = key.lower()
    valid = True
    sqr_key = int(len(key)**0.5)
    if((int(sqr_key + 0.5))**2 != len(key)):
        print("Enter a valid key!!")
        valid = False

result = [((ord(key_letters)-97) % 26) for key_letters in key]
key_matrix = [result[i:i+sqr_key] for i in range(0, len(key), sqr_key)]


def matrixMultiply(A, B):
    C = [[(sum(a*b for a, b in zip(A_row, B_col)))
          for B_col in zip(*B)] for A_row in A]
    return C


def matrix_mod_26(A):
    result = list()
    for row in A:
        result.append(row[0] % 26)
    return result


def transposeMatrix(m):
    # return [[row[i] for row in matrix] for i in range(len(matrix))]
    return list(zip(*m))


def getMinorMatrix(matrix, i, j):
    z = matrix
    z = z[:i] + z[i+1:]  # remove ith(0th) row
    # remove jth column
    for k in range(len(z)):
        z[k] = z[k][:j]+z[k][j+1:]
    return z


def determinant(matrix):
    # case ofr 2X2 matrix
    n = len(matrix)
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    det = 0
    for col in range(n):
        m = getMinorMatrix(matrix, 0, col)
        det += ((-1)**col)*matrix[0][col] * determinant(m)
    return det


def multiplicative_inverse(x, p):
    return pow(x, -1, p)


def matrixAdjugate(m):
    n = len(m)
    # case for 2X2 matrix
    if n == 2:
        return [[m[1][1], -1*m[0][1]],
                [-1*m[1][0], m[0][0]]]

    # for other cases
    # find cofactor first
    cofactor = []
    for r in range(n):
        cofactor_row = []
        for c in range(n):
            minor = getMinorMatrix(m, r, c)
            # C1,1 = (-1)**(1+1)*det
            cofactor_row.append(((-1)**(r+c))*determinant(minor))
        cofactor.append(cofactor_row)

    return transposeMatrix(cofactor)


def matrixInverse(m):
    det = determinant(m)
    print(det)
    # det*det_inverse mod 26 = 1
    det_inverse = multiplicative_inverse(det, 26)

    matrix_adjugate = matrixAdjugate(m)

    matrix_inverse = [[item*det_inverse for item in row]
                      for row in matrix_adjugate]
    return matrix_inverse


def encrypt():
    plain_text = input('Enter plain: ')
    plain_text = plain_text.lower()
    plain_text = plain_text.replace(' ', '')
    cipher_text = list()

    # add bogus letter 'x' if the length of plain text is not ideal
    while len(plain_text) % sqr_key != 0:
        plain_text += 'x'

    # divide the plain text into groups of {sqr_key} i.e row = column = n
    for x in range(0, len(plain_text), sqr_key):
        plain_text1 = []
        # plain_text1 is the smaller group of plain_text
        plain_text1 = plain_text[x:x+sqr_key]

        # create matrix for plain text with elements corresponding to the ascii values of letters
        text_matrix = [[((ord(plain_text1[i]) - 97) % 26)]
                       for i in range(len(plain_text1))]
        result_matrix = matrixMultiply(key_matrix, text_matrix)
        result_matrix = matrix_mod_26(result_matrix)

        for item in result_matrix:
            cipher_text.append(chr(item+97))

    print('Cipher text:')
    print(''.join(cipher_text))


def decrypt():
    cipher_text = input('Enter cipher text:')
    cipher_text = cipher_text.lower()
    cipher_text = cipher_text.replace(' ', '')
    plain_text = list()

    # divide the cipher text into groups of {sqr_key} i.e row = column = n
    for x in range(0, len(cipher_text), sqr_key):
        cipher_text1 = []
        cipher_text1 = cipher_text[x:x+sqr_key]

        # create matrix for cipher text with elements corresponding to the ascii values of letters
        cipher_matrix = [[((ord(cipher_text1[i]) - 97) % 26)]
                         for i in range(len(cipher_text1))]

        key_matrix_inverse = matrixInverse(key_matrix)

        result_matrix = matrixMultiply(key_matrix_inverse, cipher_matrix)
        result_matrix = matrix_mod_26(result_matrix)
        for item in result_matrix:
            plain_text.append(chr(item+97))

    print('Plain text:')
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

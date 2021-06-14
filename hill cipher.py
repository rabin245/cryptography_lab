valid = False
while not valid:
    key = input("Enter key (of length equals to a square number):")
    key = key.replace(' ', '')
    key = key.lower()
    valid = True
    sqr_key = int(len(key)**0.5)
    if((int(sqr_key + 0.5))**2 != len(key)):
        print("Enter a valid key!!")
        valid = False

result = [((ord(key_letters)-97) % 26) for key_letters in key]
key_matrix = [result[i:i+sqr_key] for i in range(0, len(key), sqr_key)]


def matrixMultiply(A, B, C):
    for i in range(len(A)):
        for j in range(len(B)):
            C[i] += A[j] * B[j][i]

    return C


def matrix_mod_26(A):
    A = [A[i] % 26 for i in range(len(A))]
    return A

def getMinorMatrix(matrix, i, j):
    z = matrix
    z = z[:i] + z[i+1:]  # remove ith(0th) row
    # remove jth column
    for k in range(len(z)):
        z[k] = z[k][:j]+z[k][j+1:]
    return z


def det(matrix, n):
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    sum = 0
    for col in range(n):
        m = getMinorMatrix(matrix, 0, col)
        sum = sum + ((-1)**col)*matrix[0][col] * det(m, n-1)
    return sum

def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix))]

def adjugateMatrix(M):
    n = len(M)
    if n == 2:
        return [[M[1][1], -1*M[0][1]],
                [-1*M[1][0], M[0][0]]]
    cofactor = []
    for r in range(n):
        cofactor_row = []
        for c in range(n):
            minor=getMinorMatrix(M,r,c)
            cofactor_row.append(((-1)**(r+c))*det(minor,len(minor)))
        cofactor.append(cofactor_row)

    return transpose(cofactor)
    

def inverseMatrix(matrix):
    d = det(matrix, len(matrix))

    found = False
    d_inverse = 1
    # d*d_inverse mod 26 = 1 
    while not found:
        if((d*d_inverse) % 26 == 1):
            found = True
        else:
            d_inverse += 1
    
    matrix_adjugate = adjugateMatrix(key_matrix)

    matrix_adjugate = [[item*d_inverse for item in row] for row in matrix_adjugate ]
    return matrix_adjugate

def encrypt():
    plain_text = input('Enter plain: ')
    plain_text = plain_text.lower()
    plain_text = plain_text.replace(' ','')
    cipher_text = list()
    
    # add bogus letter 'x' if the length of plain text is not ideal
    while len(plain_text)%sqr_key!=0:
        plain_text+='x'
    
    # divide the plain text into groups of {sqr_key} i.e row = column = n
    for x in range(0, len(plain_text), sqr_key):
        plain_text1=[]
        plain_text1=plain_text[x:x+sqr_key]             # plain_text1 is the smaller group of plain_text
        
        # create matrix for plain text with elements corresponding to the ascii values of letters
        text_matrix = [((ord(plain_text1[i]) - 97) % 26)
                    for i in range(len(plain_text1))]

        result_matrix = [0]*sqr_key     # zero matrix of 1 X sqr_key size
        result_matrix = matrixMultiply(text_matrix, key_matrix, result_matrix)
        result_matrix = matrix_mod_26(result_matrix)

        for item in result_matrix:
            cipher_text.append(chr(item+97))
    print('Cipher text: ')
    print(''.join(cipher_text))


def decrypt():
    cipher_text = input('Enter cipher text:')
    cipher_text = cipher_text.lower()
    cipher_text = cipher_text.replace(' ','')
    plain_text = list()

    # divide the cipher text into groups of {sqr_key} i.e row = column = n
    for x in range(0, len(cipher_text), sqr_key):
        cipher_text1=[]
        cipher_text1=cipher_text[x:x+sqr_key] 
        
        # create matrix for cipher text with elements corresponding to the ascii values of letters
        cipher_matrix = [((ord(cipher_text1[i]) - 97) % 26)
                     for i in range(len(cipher_text1))]

        result_matrix = [0]*sqr_key
        key_matrix_inverse = inverseMatrix(key_matrix)
        result_matrix = matrixMultiply(cipher_matrix, key_matrix_inverse, result_matrix)
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

# a = 97
# x = input()
# for char in x:
#     print(ord(char))

# x = " "
# print(x.isupper())
# print(ord(x))

# a = -62 % 26
# print(a)
# a += 97
# print(a)
# print(chr(a))

# string = "hello"
# # print(list(string))
# string = list(string)
# print(string)

# key_keys = "abcdefghijklmnopqrstuvwxyz"
# key_values = "qwertyuiopasdfghjklzxcvbnm"
# key_keys = list(key_keys)
# key_values = list(key_values)

# # encryption_dict = {key_keys[i] : key_values[i] for i in range(len(key_keys))}
# encryption_dict = dict (zip(key_keys, key_values))
# print(encryption_dict.get('a'))

# x = ' '
# x = x.lower()
# print(x, "asf")

# x = 'abcd'
# s = x.find('c')
# print(s)

# letters = list('abcdefghiklmnopqrstuvwxyz')

# letter = 'h'
# # print(letters.index(letter))
# temp = letters.index(letter)
# remainder = temp % 5
# div = temp // 5
# print(div, remainder)


# key = ['m', 'o', 'n', 'a', 'r', 'c', 'h', 'y', 'b', 'd', 'e', 'f',
#        'g', 'i', 'k', 'l', 'p', 'q', 's', 't', 'u', 'v', 'w', 'x', 'z']
# ciphertext = list('help')

# if(len(ciphertext)%2!=0):
#     ciphertext.append('z')

# index_first = []
# index_second = []
# for i in range(len(ciphertext)):
#     if(i % 2 == 0):
#         index_first.append(key.index(ciphertext[i]))

#     else:
#         index_second.append(key.index(ciphertext[i]))

# print(index_first)
# print(index_second)
# cipher = []
# for i in range(len(index_first)):
#     row_first = index_first[i] // 5
#     col_first = index_first[i] % 5
#     row_second = index_second[i] // 5
#     col_second = index_second[i] % 5

#     if(row_first == row_second):
#         col_first = (col_first + 1) % 5
#         col_second = (col_second + 1) % 5

#     elif(col_first == col_second):
#         row_first = (row_first + 1) % 5
#         row_second = (row_second + 1) % 5

#     else:
#         col_first, col_second = col_second, col_first

#     index_first_temp = row_first * 5 + col_first
#     index_second_temp = row_second * 5 + col_second

#     cipher.append(index_first_temp)
#     cipher.append(index_second_temp)


# ciphertext = []
# for x in cipher:
#     ciphertext.append(key[x])
# print(ciphertext)
# print(''.join(ciphertext))
# print(''.join(ciphertext))

# matrix = [[1, 2, 3],
#           [4, 5, 6], [7, 8, 9]]
# for i in range(matrix):
#     for j in range(matrix(i)):
#         print(i,j)

# characters = [chr(i) for i in range(97, 123)]
# print(characters.index('i'))
# # 105
# if 'i' in characters:
#     print(chr(73))

# msg = 'hello'

# for s in range(0, len(msg)):
#     print(s,len(msg))
#     if msg[s] == msg[s+1]:
#         msg = msg[:s+1]+'X'+msg[s+1:]
#     print(s,len(msg))
# msg = 'hell'
# # h l
# for s in range(0, len(msg), 2):
#     if s < len(msg)-1:
#         if msg[s] == msg[s+1]:
#             msg = msg[:s+1]+'X'+msg[s+1:]
# if len(msg) % 2 != 0:
#     msg = msg[:]+'X'

# print(msg)

# s = -1
# print(s%2)
# key = 'heerr'
# print((int(pow(len(key),0.5) + 0.5))**2)
# if(int(pow(len(key),0.5)) + 0.5) ** 2 == len(key)):
#     pass
# x=4
# print(x**0.5)

# A = [[1,20,3],[1,2,3],[1,2,3]]
# # A = [A[i]%5 for i in range(len(A))]
# # print(A)
# B = A
# i=1
# B = B[:i]+B[i+1:]
# print(B)
# def minor(array,i,j):
#     c = array
#     c = c[:i] + c[i+1:]
#     for k in range(0,len(c)):
#         c[k] = c[k][:j]+c[k][j+1:]
#     return c
# def det(array,n):
#     if n == 1 :return array[0][0]
#     if n == 2 :return array[0][0]*array[1][1] - array[0][1]*array[1][0]
#     sum = 0
#     for i in range(0,n):
#         m = minor(array,0,i)
#         sum =sum + ((-1)**i)*array[0][i] * det(m,n-1)
#     return sum
# def multip(X, Y):
#     return [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
# B = [[1,2,3],[4,5,2],[1,4,3]]
# A = [[1,2,3]]
# C=[1,2,3]
# # print(multip(A,B))
# print(list(zip(*B)))
# print(list(zip(C,B)))

# def transpose(matrix):
#     return [[row[i] for row in matrix] for i in range(len(matrix))]

# A = [[1,2,3],[4,5,2],[1,4,3]]
# # print(transpose(B))
# # A = [[row[i]*10 for row in A] for i in range(len(A))]
# A = [[item*10 for item in row] for row in A ]
# print(A)

# x = 3
# y = 1
# while(True):
#     if (x*y)%26==1 :
#         break
#     else:
#         y+=1

# print(y)

# x =dict()
# x = {chr(i):((i-97)%26) for i in range(97,123)}
# print(x)

# def getMinorMatrix(matrix, i, j):
#     z = matrix
#     z = z[:i] + z[i+1:]  # remove ith(0th) row
#     # remove jth column
#     for k in range(len(z)):
#         z[k] = z[k][:j]+z[k][j+1:]
#     return z


# def det(matrix, n):
#     if n == 2:
#         return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
#     sum = 0
#     for col in range(n):
#         m = getMinorMatrix(matrix, 0, col)
#         sum = sum + ((-1)**col)*matrix[0][col] * det(m, n-1)
#     return sum

# A = [[2,8,15],[7,4,17],[8,13,16]]
# B = [[4,17],[13,16]]
# c=[[7,17],[8,16]]
# d=[[7,4],[8,13]]
# e=[[8,15],[13,16]]

# k = [[-157,67,76],[24,-88,71],[59,38,-48]]

# k = [[3*item for item in row] for row in k]

# k = [[item%26 for item in row] for row in k]

# x = [76 ,209, 350]
# x = [item%26 for item in x]
# print(k)

# result = [824, 598, 629]
# result = [item%26 for item in result]
# print(result)

# sqr_key = 3

# plain_text = 'suss'
# while len(plain_text)%sqr_key!=0:
#     plain_text += 'x'

# print(plain_text)
# for x in range(0, len(plain_text), sqr_key):
#     plain_text1=[]
#     plain_text1=plain_text[x:x+sqr_key]
#     print(plain_text1)


# c = 'balz'
# k=3
# for char in c:
#     plain_ascii = ord(char)
#     plain_range = ord(char)

# key = 'monarchy'
# myset=set()
# for i in range(len(key)):
#     myset.add(key[i])
# print(myset)
# print(list(myset))

# key = 'dece'
# result = list()
# result.extend(key)
# print(result)

# length = 18

# while not reached:
# current_letter = (ciphertext[i]-key[i])%26
# key.append(current_letter)
#   print(current_letter)
#     for char in key:
#         result.append(char)
#         if(len(result)==length):
#             print('reached')
#             reached = True
#             break

# print(result)

# key = 'abz'
# key = [(ord(char)-97) for char in key]
# print(key)

# lst = {chr(i):i-97 for i in range(97,123)}
# print(lst)

# import random
# x = random.randint(0,3)
# print(x)

key = 'ab'
ciphertext = 'hfspz'
key = [ord(i)-97 for i in key]
ciphertext = [ord(i)-97 for i in ciphertext]
plaintext = []
for i in range(len(ciphertext)):
    current_letter = (ciphertext[i]-key[i]) % 26

    if len(key) < len(ciphertext):
        key.append(current_letter)
    print(current_letter)
    plaintext.append(chr(current_letter+97))

print(key)
print(plaintext)

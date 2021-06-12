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
# plaintext = list('help')

# if(len(plaintext)%2!=0):
#     plaintext.append('z')

# index_first = []
# index_second = []
# for i in range(len(plaintext)):
#     if(i % 2 == 0):
#         index_first.append(key.index(plaintext[i]))

#     else:
#         index_second.append(key.index(plaintext[i]))

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
# print(''.join(plaintext))
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

s = -1
print(s%2)
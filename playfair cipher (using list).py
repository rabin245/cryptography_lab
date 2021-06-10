letters = list('abcdefghiklmnopqrstuvwxyz')
key = list('monarchy')
plaintext = list('baaaoon')

for letter in key:
    letters.remove(letter)

key.extend(letters)

if(len(plaintext) % 2 != 0):
    plaintext.append('z')

index_first = []
index_second = []
for i in range(len(plaintext)):
    if(i % 2 == 0):
        index_first.append(key.index(plaintext[i]))
    else:
        index_second.append(key.index(plaintext[i]))

# for i in range(len(index_first)):
#     if(index_first[i]==index_second[i]):
#         pass       

print(index_first)
print(index_second)
cipher = []
for i in range(len(index_first)):
    row_first = index_first[i] // 5
    col_first = index_first[i] % 5
    row_second = index_second[i] // 5
    col_second = index_second[i] % 5

    if(row_first == row_second):
        col_first = (col_first + 1) % 5
        col_second = (col_second + 1) % 5

    elif(col_first == col_second):
        row_first = (row_first + 1) % 5
        row_second = (row_second + 1) % 5

    else:
        col_first, col_second = col_second, col_first

    index_first_temp = row_first * 5 + col_first
    index_second_temp = row_second * 5 + col_second

    cipher.append(index_first_temp)
    cipher.append(index_second_temp)


ciphertext = []
for x in cipher:
    ciphertext.append(key[x])
print(ciphertext)
print(''.join(plaintext))
print(''.join(ciphertext))

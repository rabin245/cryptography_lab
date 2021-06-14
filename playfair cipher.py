
letters = list('abcdefghiklmnopqrstuvwxyz')
key = list('monarchy')
plaintext = list('helps')


for letter in key:
    letters.remove(letter)

key.extend(letters)
print(str(key))
table = [key[i:i+5] for i in range(0, len(key), 5)]
print(table)

if(len(plaintext) % 2 != 0):
    plaintext.append('z')

# for i in range(0, len(plaintext), 2):
#     temp_letter = plaintext[i]

plaintext = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]
flag1 = []
flag2 = []
for i in range(len(plaintext)):
    for j in range(len(table)):
        for k in range(5):
            if(plaintext[i][0] == table[j][k]):
                flag1.append([j, k])
            if(plaintext[i][1] == table[j][k]):
                flag2.append([j, k])
print(flag1)
print(flag2)
for i in range(len(plaintext)):
    if (flag1[i][0] == flag2[i][0]):
        flag1[i][1] = (flag1[i][1]+1) % 5
        flag2[i][1] = (flag2[i][1]+1) % 5
    elif(flag1[i][1] == flag2[i][1]):
        flag1[i][0] = (flag1[i][0]+1) % 5
        flag2[i][0] = (flag2[i][0]+1) % 5
    else:
        flag1[i][1], flag2[i][1] = flag2[i][1], flag1[i][1]
cipher=[]
for i in range(len(plaintext)):
    temp1 = table[flag1[i][0]][flag1[i][1]]
    temp2 = table[flag2[i][0]][flag2[i][1]]
    cipher.append(temp1)
    cipher.append(temp2)

print(str(cipher))
        
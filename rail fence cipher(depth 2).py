def encrypt():
    plaintext = str(input("enter plaintext:"))
    plaintext = plaintext.lower()   
    plaintext = plaintext.replace(' ', '')
    plaintext = list(plaintext)

    temp1 = list()
    temp2 = list()
    ciphertext = list()

    for i in range(0, len(plaintext)):
        if i%2==0:
            temp1.append(plaintext[i])
        else:
            temp2.append(plaintext[i])
    
    ciphertext.extend(temp1)
    ciphertext.extend(temp2)
    print('Cipher text: ')
    print(''.join(ciphertext))

def decrypt():
    ciphertext = str(input("enter ciphertext:"))
    ciphertext = ciphertext.lower()   
    ciphertext = ciphertext.replace(' ', '')
    ciphertext = list(ciphertext)
    plaintext = list()
    if len(ciphertext)%2!=0:
        ciphertext.append('x')
    length = len(ciphertext)
    ciphertext = [ciphertext[i:i+length//2] for i in range(0,len(ciphertext), length//2)]
    plaintext = [row[i]  for i in range(len(ciphertext[0])) for row in ciphertext]
    # for i in range(len(ciphertext[0])):
    #     for row in ciphertext:
    #         ciphertext1.append(row[i])
    # print(ciphertext1)
    print('Plain text: ')
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

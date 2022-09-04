#This python script encrypts/decrypts your passwords saved in a .txt format using a password.
#Receives the parameters encrypt and decrypt.
#You can not encrypt over an already encrypted file.
#Prevents rainbow tables attacks with salting.
#Only accepts ASCII characters for now

#Creates a folder called "encrypted passwords" with the encrypted content

import sys
from encrypt import encrypt
from decrypt import decrypt

def run():
    #If first parameter is encrypt
    if sys.argv[1] == "encrypt":
        file = sys.argv[2]
        password = input("Select a password for encryption:  ")
        #encrypt file with password
        encrypt(password, file)

    #If first parameter is decrypt
    if sys.argv[1] == "decrypt":
        file = sys.argv[2]
        password = input("Select a password for decryption:  ")
        salt_file = sys.argv[3]
        #decrypt file with password
        decrypt(file, password, salt_file)
        ####Code below for future implementation of automatic salt finder
        # if len(sys.argv) >= 4:
        #     decrypt(file, password, sys.argv[3])
        # else:
        #     decrypt(file, password)



if __name__ == '__main__':
    run()
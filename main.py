#This python script encrypts/decrypts your passwords saved in a .txt format using a password.
#Receives the parameters encrypt and decrypt.
#You can not encrypt over an already encrypted file.
#Prevents rainbow tables attacks with salting.
#Only accepts ASCII characters for now

#Creates a folder called "encrypted passwords" with the encrypted content

import sys
from encrypt import encrypt

def run():
    #If first parameter is encrypt
    if sys.argv[1] == "encrypt":
        file = sys.argv[2]
        password = input("Select a password for file encryption:  ")
        #encrypt file with password
        encrypt(password)

    #If first parameter is decrypt
    if sys.argv[1] == "decrypt":
        print("desencripte tu archivo je")


if __name__ == '__main__':
    run()
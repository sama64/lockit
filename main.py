#This python script encrypts/decrypts your passwords saved in a .txt format using a password.
#Receives the parameters encrypt and decrypt.
#You can not encrypt over an already encrypted file.
#Prevents rainbow tables attacks with salting.
#Only accepts ASCII characters for now

#Creates a folder called "encrypted passwords" with the encrypted content

import sys
import os
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

        #if user especified salt, use. If not, try default
        if len(sys.argv) >= 4:
            decrypt(file, password, sys.argv[3])
        else:
            #looking for salt
            print(f"Salt may be in: {os.path.dirname(file)}/salt")
            try:
                file_dir = os.path.dirname(file)
                decrypt(file, password, f"{file_dir}/salt")
            except:
                print("Salt not found. Especify salt path")



if __name__ == '__main__':
    run()
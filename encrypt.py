import os
from cryptography.fernet import Fernet
from generate_key import generate_key

#encrypts a file with the password
#recives str:password str:file
def encrypt(password, file):

    print(f"Encrypting {file}...")

    #generates the key and salt with the given password
    key, salt = generate_key(password)

    #encrypts file contents
    with open(file, "rb") as file:
        contents = file.read()
    contents_encrypted = Fernet(key).encrypt(contents)

    #creates a directory for encrypted file and salt
    try: 
        os.mkdir("encrypted_passwords")
    except:
        print("encrypted_passwords directory already exists. Overwriting it.")

    #writes salt
    with open("./encrypted_passwords/salt", "wb") as file:
        file.write(salt)
    
    #writes encrypted passwords
    print(file)
    with open(f"./encrypted_passwords/passwords", "wb") as file:
        file.write(contents_encrypted)

    #inform user
    print(f"Done. Encrypted contents in {os.getcwd()}/encrypted_passwords")
    print("Remember to keep the salt in the same directory to decrypt later.")
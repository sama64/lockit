import os
from cryptography.fernet import Fernet
from generate_key import generate_key

#decrypts a given file
#receives str:filename str:password optional str:salt
def decrypt(filename, password, salt_file):
    #user inputs password to decrypt

    # DEPRECATED reading salt
    # salt = b''
    # if salt_file == "salt":
    #     print(str(os.path.dirname(file)))
    #     with open(f"{os.path.dirname}{salt_file}", "rb") as file:
    #         salt = file.read()
    # else:
    #     with open(salt_file, "rb") as file:
    #         salt = file.read()

    #reading salt
    with open(salt_file, "rb") as file:
        salt = file.read()


    print("Generating key...")
    #generating decryption key with password and salt
    key, salt_returned = generate_key(password, salt)
    print(f"key: {key} | salt: {str(salt)}")

    print("Decrypting contents...")
    #decrypting passwords
    with open(filename, "rb") as file:
        contents = file.read()
    decrypted_contents = Fernet(key).decrypt(contents)

    #writing decrypted password file
    with open("passwords.txt", "wb") as file:
        file.write(decrypted_contents)

    print(f"Done. Decrypted contents in {os.getcwd()}/passwords.txt")
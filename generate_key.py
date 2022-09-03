import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

#generates a key accepted for fernet from a given password
#receives string:password  optional b:salt
#returns b:key b:salt to be used/stored.
def generate_key(password, salt=os.urandom(16)):

    #parsing password to bytes
    password = bytes(password, 'ascii')

    #generating hash with salt to resist rainbow tables attack
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))

    return key, salt


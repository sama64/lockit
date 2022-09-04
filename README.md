# passcrypt
This python script encrypts/decrypts your passwords saved in a .txt format using a password. It uses AES128(Fernet) for encryption.

## Features:
- Creates a folder called "encrypted passwords" with the encrypted content.
- Prevents rainbow tables attacks with salting.
- Only accepts ASCII characters for now.

## Usage:
Receives the parameters encrypt or decrypt, and following the file.
When decrypting it is necessary to add the salt as the last parameter (It will be automatic later). The salt is saved in the encrypted_passwords folder.

## Examples:
#### Encryption
`python3 main.py encrypt mypasswords.txt`
#### Decryption
`python3 main.py decrypt mypasswords salt`

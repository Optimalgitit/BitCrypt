from EncryptionWare import EncryptionWare
from getpass import getpass


TO_ENCRYPT = input("Please enter the text you would like to encrypt: ")
PASS = getpass()

Encrypt = EncryptionWare(TO_ENCRYPT, PASS)
Encrypt.encrypt_verbose()

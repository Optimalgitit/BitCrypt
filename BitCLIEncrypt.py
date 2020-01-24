from BitLib import BitLib
from getpass import getpass


TO_ENCRYPT = input("Please enter the text you would like to encrypt: ")
PASS = getpass(prompt="Enter Password: ")

Encrypt = BitLib(TO_ENCRYPT, PASS)
Encrypt.encrypt_verbose()

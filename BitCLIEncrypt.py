from BitLib import BitLib
from getpass import getpass
import pyperclip as pyclip

TO_ENCRYPT = input("Please enter the text you would like to encrypt: ")
PASS = getpass(prompt="Enter Password: ")

Encrypt = BitLib(TO_ENCRYPT, PASS)
Encrypted = Encrypt.encrypt_verbose()
pyclip.copy(Encrypted)

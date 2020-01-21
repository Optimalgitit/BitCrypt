from EncryptionWare import EncryptionWare

TO_ENCRYPT = input("Please enter the text you would like to decrypt: ")
PASS = input("Enter Password: ")

Encrypt = EncryptionWare(TO_ENCRYPT, PASS)
Encrypt.decrypt_verbose()

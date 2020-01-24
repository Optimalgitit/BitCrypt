import hashlib as _hashlib

class BitLib:
    def __init__(self, string, key):
        self.string = string
        self.key = key
    def encrypt_verbose(self):
        import tqdm as _tqdm # TQDM is only needed for verbose mode
        key = self.key.encode() # Create the non-public key and encode it into bytes
        for i in _tqdm.tqdm(key, desc="Generating key hash", unit="hashe(s)"): # Do this for the amount of characters in the key
            key = f"{_hashlib.sha512(key).hexdigest()}{i}".encode() # Encrypt the key using SHA-512
        print('Converting key back to unicode')
        key = key.decode() # Convert key back to unicode
        key = int(''.join([str(ord(i)) for i in _tqdm.tqdm(key, desc="Converting key hash to a number", unit="char(s)")])) # Convert each character into a keycode number so it is workable
        key = int(str(key)[:16]) # Trim key to 16 characters to avoid integer overflow
        string = '-'.join([str(ord(i) + key) for i in _tqdm.tqdm(self.string, desc="Converting and Encrypting string", unit="char(s)")]) # Convert each character into a keycode to make it workable, then add the key to each character for the actual encryption
        print(string)
        return string
    def encrypt(self):
        key = self.key.encode()
        for i in key: # Do this for the amount of characters in the key
            key = f"{_hashlib.sha512(key).hexdigest()}{i}".encode() # Encrypt the key using SHA-512
        key = key.decode() # Convert key back to unicode
        key = int(''.join([str(ord(i)) for i in key])) # Convert each character into a keycode number so it is workable
        key = int(str(key)[:16]) # Trim key to 16 characters to avoid integer overflow
        string = '-'.join([str(ord(i) + key) for i in self.string]) # Convert each character into a keycode to make it workable, then add the key to each character for the actual encryption
        return string
    def decrypt_verbose(self):
        import tqdm as _tqdm # TQDM is only needed for verbose mode
        key = self.key.encode()
        for i in _tqdm.tqdm(key, desc="Generating key hash", unit="hashe(s)"): # Do this for the amount of characters in the key
            key = f"{_hashlib.sha512(key).hexdigest()}{i}".encode() # Encrypt the key using SHA-512
        print('Converting key back to unicode')
        key = key.decode() # Convert key back to unicode
        key = int(''.join([str(ord(i)) for i in _tqdm.tqdm(key, desc="Converting key hash to a number", unit="char(s)")])) # Convert each character into a keycode number so it is workable
        key = int(str(key)[:16]) # Trim key to 16 characters to avoid integer overflow
        print(key)
        string = ''.join([str(chr(int(i) - key)) for i in _tqdm.tqdm(self.string.split('-'), desc="Converting and Decrypting string", unit="char(s)")]) # Convert each character into a keycode to make it workable, then add the key to each character for the actual encryption
        print(string)
        return string
    def decrypt(self):
        key = self.key.encode()
        for i in key: # Do this for the amount of characters in the key
            key = f"{_hashlib.sha512(key).hexdigest()}{i}".encode() # Encrypt the key using SHA-512
        key = key.decode() # Convert key back to unicode
        key = int(''.join([str(ord(i)) for i in key])) # Convert each character into a keycode number so it is workable
        key = int(str(key)[:16]) # Trim key to 16 characters to avoid integer overflow
        string = ''.join([str(chr(int(i) - key)) for i in self.string.split('-')]) # Convert each character into a keycode to make it workable, then add the key to each character for the actual encryption
        return string
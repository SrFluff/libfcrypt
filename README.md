# LibFcrypt

Simple, symmetric encryption. Courtesy of cryptography and Fernet.

## Functions

### Base

- `base.check_key(key)`: Check a key's (bytes) validity, returns a boolean.
- `base.gen_key()`: Generate a bytes object key.
- `base.passwd_gen_key(passwd)`: Generate a bytes object key derived from a string.
- `base.encrypts(key,string)`: Encrypt a string using a key (bytes), returns a bytes object.
- `base.encryptb(key,dataBytes)`: Encrypt a bytes object using a key (bytes), returns a bytes object.
- `base.decrypts(key,string)`: Decrypt a bytes object using a key (bytes), returns a string.
- `base.decryptb(key,byteString)`: Decrypt a bytes object using a key (bytes), returns a bytes object.

### File

- `file.encryptf(key,filePtr)`: Encrypt the contents of a file using a key (bytes), returns a bytes object.
- `file.encryptbf(key,filePtr)`: Encrypt the contents of a file using a key (bytes), returns a bytes object.
- `file.decryptf(key,filePtr)`: Decrypt the contents of a file using a key (bytes), returns a string.
- `file.decryptbf(key,filePtr)`: Decrypt the contents of a file using a key (bytes), returns a bytes object.

## Variables

- `VERSION`: Module version information, string.
- `LICENSE`: Module licensing information, string.

## Errors

- `errors.InvalidKey`: Should be raised when `base.check_key()` returns `False`.

## Installation

### Git

```sh
git clone https://www.github.com/SrFluff/libfcrypt
cd libfcrypt
cp -r libfcrypt $PYTHONPATH
```

### Pip

```sh
pip install libfcrypt
```

```python
import libfcrypt

# Generate a key
key = libfcrypt.base.gen_key()

# Generate a key from a password
other_key = libfcrypt.base.passwd_gen_key("Password123")

# Encrypt a string
secrets = libfcrypt.base.encrypts(key,"I have so many secrets muahaha!")

# Encrypt a bytes object
bSecrets = libfcrypt.base.encryptb(key,b'ID3')

# Write secrets to a file
with open("Secrets.txt","wb") as f:
    f.write(secrets)

# Read secrets from a file

f = open("Secrets.txt","rb")
spilled_secrets = libfcrypt.file.decryptf(key,f)

# Spill secrets!

print(spilled_secrets)
```

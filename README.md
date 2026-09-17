# LibFcrypt

Simple, symmetric encryption. Courtesy of cryptography and Fernet.


## Functions

- `base.gen_key()`: Generate a bytes object key.
- `base.encrypts(key,string)`: Encrypt a string using a key (bytes), returns a bytes object.
- `base.decrypts(key,string)`: Decrypt a string using a key (bytes), returns a string.

- `file.encryptf(key,filePtr)`: Encrypt the contents of a file using a key (bytes), returns a bytes object.
- `file.decryptf(key,filePtr)`: Decrypt the contents of a file using a key (bytes), returns a string.

## Variables

- `VERSION`: Module version information, string.
- `LICENSE`: Module licensing information, string.

## Installation

Copy the `libfcrypt/` directory to your `$PYTHONPATH` directory, and import it like so:
```python
import libfcrypt

```

## Usage

```python
import libfcrypt

# Generate a key
key = libfcrypt.base.gen_key()

# Encrypt a string
secrets = libfcrypt.encrypts(key,"I have so many secrets muahaha!")

# Write secrets to a file
with open("Secrets.txt","wb") as f:
    f.write(secrets)

# Read secrets from a file

f = open("Secrets.txt","rb")
spilled_secrets = libfcrypt.file.decryptf(key,f)

# Spill secrets!

print(spilled_secrets)
```

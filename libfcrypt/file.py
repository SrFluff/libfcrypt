from libfcrypt.base import decrypts, encrypts


def encryptf(key,filePtr):
    return encrypts(key,filePtr.read())

def decryptf(key,filePtr):
    return decrypts(key,filePtr.read())

import base
import errors


def encryptf(key,filePtr) -> bytes:
    if not base.check_key(key):
        raise errors.InvalidKey("Invalid key passed.")
    return base.encrypts(key,filePtr.read())

def encryptbf(key,filePtr) -> bytes:
    if not base.check_key(key):
        raise errors.InvalidKey("Invalid key passed.")
    return base.encryptb(key,filePtr.read())

def decryptf(key,filePtr) -> str:
    if not base.check_key(key):
        raise errors.InvalidKey("Invalid key passed.")
    return base.decrypts(key,filePtr.read())

def decryptbf(key,filePtr) -> bytes:
    if not base.check_key(key):
        raise errors.InvalidKey("Invalid key passed.")
    return base.decryptb(key,filePtr.read())

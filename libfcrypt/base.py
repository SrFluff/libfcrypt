import base64
import hashlib

from cryptography.fernet import Fernet

from . import errors


def check_key(key: bytes) -> bool:
    try:
        Fernet(key)
        return True
    except ValueError:
        return False

def gen_key() -> bytes:
    return Fernet.generate_key()

def passwd_gen_key(passwd:str) -> bytes:
    hashed_passwd = hashlib.sha256(passwd.encode()).digest()
    encoded_passwd = base64.urlsafe_b64encode(hashed_passwd)
    return encoded_passwd

def encryptb(key:bytes,dataBytes:bytes) -> bytes:
    if not check_key(key):
        raise errors.InvalidKey("Invalid key passed")
    return Fernet(key).encrypt(dataBytes)

def encrypts(key:bytes,string:str) -> bytes:
    if not check_key(key):
        raise errors.InvalidKey("Invalid key passed")
    return Fernet(key).encrypt(string.encode())

def decrypts(key:bytes,byteString:bytes) -> str:
    if not check_key(key):
        raise errors.InvalidKey("Invalid key passed")
    return Fernet(key).decrypt(byteString).decode()

def decryptb(key:bytes,byteString:bytes) -> bytes:
    if not check_key(key):
        raise errors.InvalidKey("Invalid key passed")
    return Fernet(key).decrypt(byteString)

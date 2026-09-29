import base64
import hashlib

from cryptography.fernet import Fernet


def gen_key() -> bytes:
    return Fernet.generate_key()

def passwd_gen_key(passwd:str) -> bytes:
    hashed_passwd = hashlib.sha256(passwd.encode()).digest()
    encoded_passwd = base64.urlsafe_b64encode(hashed_passwd)
    return encoded_passwd

def encrypts(key:bytes,string:str) -> bytes:
    return Fernet(key).encrypt(string.encode())

def decrypts(key:bytes,bytestring:bytes) -> str:
    return Fernet(key).decrypt(bytestring).decode()

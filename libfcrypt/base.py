from cryptography.fernet import Fernet


def gen_key() -> bytes:
    return Fernet.generate_key()

def encrypts(key:bytes,string:str) -> bytes:
    return Fernet(key).encrypt(string.encode())

def decrypts(key:bytes,bytestring:bytes) -> str:
    return Fernet(key).decrypt(bytestring).decode()

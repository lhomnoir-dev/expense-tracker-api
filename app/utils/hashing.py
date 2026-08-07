from argon2 import PasswordHasher

pswd_hasher = PasswordHasher()


def hash_password(password: str) -> str:
    return pswd_hasher.hash(password)


def verify_password(hashed_password: str, password: str) -> bool:
    return pswd_hasher.verify(hashed_password, password)

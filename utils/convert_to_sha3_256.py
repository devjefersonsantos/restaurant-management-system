from hashlib import sha3_256

def convert_to_sha3_256(value) -> str:
    return sha3_256(value.encode()).hexdigest()

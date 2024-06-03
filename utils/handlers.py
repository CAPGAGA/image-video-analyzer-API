import hashlib

# generate random filename
async def generate_hash_key(file_name:str) -> str:
    key = hashlib.sha256(str(file_name).encode()).hexdigest()
    return str(key)
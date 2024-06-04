import hashlib
import uuid
import time

# generate random filename
async def generate_hash_key() -> str:
    key = f"{int(time.time())}_{uuid.uuid4().hex}"
    return str(key)
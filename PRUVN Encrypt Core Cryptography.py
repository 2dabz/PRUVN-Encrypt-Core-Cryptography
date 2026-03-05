#PRUVN Encrypt AES-256-GCM File Encryption - MIT License 

from Crypto.Cipher import AES
from argon2.low_level import hash_secret_raw, Type

# Encrypt

salt = secrets.token_bytes(32)
key = hash_secret_raw(secret=password.encode(), salt=salt, time_cost=3,
                      memory_cost=64 * 1024, parallelism=4, hash_len=32, type=Type.ID)
encrypt_cipher = AES.new(key, AES.MODE_GCM)

outfile.write(salt)
outfile.write(encrypt_cipher.nonce)
outfile.write(encrypt_cipher.digest())

# Decrypt

salt = infile.read(32)
nonce = infile.read(16)
infile.seek(header_size + ciphertext_size)
tag = infile.read(tag_size)
key = hash_secret_raw(secret=password.encode(), salt=salt, time_cost=3,
                      memory_cost=64 * 1024, parallelism=4, hash_len=32, type=Type.ID)
decrypt_cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
decrypt_cipher.verify(tag)